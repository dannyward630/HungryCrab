from __future__ import annotations

import json
from pathlib import Path

import pytest
from helpers import copy_repo

from hungry_crab.compare import CompareOptions, compare_digests, menu_candidates
from hungry_crab.digest import DigestResult
from hungry_crab.errors import CrabError
from hungry_crab.ledger import Ledger
from hungry_crab.licensing.policy import apply_maw_policy, nutrient_material
from hungry_crab.maw import MawConfig
from hungry_crab.nutrients import Candidate, Evidence
from hungry_crab.serve import ServeOptions, render_issue, serve


@pytest.mark.parametrize("mode", ["HUMAN", "IDEAS_ONLY", "REIMPLEMENT"])
def test_strict_never_widens_a_mode(mode: str) -> None:
    assert apply_maw_policy(mode, policy="strict", material="code") == (mode, "")


def test_strict_policy_retains_configs_and_templates() -> None:
    for material in ("configuration", "template"):
        assert apply_maw_policy("COPY", policy="strict", material=material) == ("COPY", "")
    assert nutrient_material("ci", [".github/workflows/ci.yml"]) == "configuration"
    assert nutrient_material("tests", ["tests/test_core.py"]) == "code"
    assert nutrient_material("tests", ["vitest.config.ts"]) == "configuration"
    assert nutrient_material("future-category", []) == "code"


@pytest.mark.parametrize("mode", ["COPY", "COPY_FILE"])
def test_strict_requires_cleanroom_for_every_code_copy_mode(mode: str) -> None:
    result, reason = apply_maw_policy(mode, policy="strict", material="code")
    assert result == "REIMPLEMENT" and mode in reason
    assert apply_maw_policy(mode, policy="strict", material="configuration") == (mode, "")


@pytest.mark.parametrize(
    "paths",
    [
        [],
        ["tests/run.sh"],
        ["tools/validate.lua"],
        ["test.mjs"],
        ["test.ps1"],
        ["evil.config.py"],
        ["unknown.config.js"],
        ["test.unknown"],
        ["ci.yml", "run.sh"],
    ],
)
def test_unknown_scripts_and_missing_evidence_are_code(paths: list[str]) -> None:
    assert nutrient_material("tests", paths) == "code"


@pytest.mark.parametrize("license_id", ["MIT", "MPL-2.0"])
def test_real_menu_keeps_only_recognized_config_copy_permissions(
    npm_digest: DigestResult, py_digest: DigestResult, tmp_path: Path, license_id: str
) -> None:
    prey = copy_repo(npm_digest.out_dir, tmp_path / "prey")
    path = prey / "license.json"
    license_data = json.loads(path.read_text(encoding="utf-8"))
    license_data["spdx"] = license_id
    path.write_text(json.dumps(license_data), encoding="utf-8")
    manifest_path = prey / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for entry in manifest["files"]:
        if entry["name"] == "license.json":
            entry["bytes"] = path.stat().st_size
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    normal = compare_digests(prey, py_digest.out_dir, options=CompareOptions(maw_license="MIT"))
    strict = compare_digests(
        prey, py_digest.out_dir, options=CompareOptions(maw_license="MIT", mode="strict")
    )
    legal = "COPY" if license_id == "MIT" else "COPY_FILE"
    assert normal.verdict["mode"] == legal
    architecture = next(card for card in strict.candidates if card.category == "architecture")
    assert architecture.license_mode == "REIMPLEMENT"
    assert architecture.material == "code" and legal in architecture.trace["maw_policy_reason"]
    config = next(card for card in strict.candidates if card.id == "crab:ci:ci.cache")
    assert config.license_mode == legal and config.material == "configuration"


def test_same_prey_strict_and_normal_modes_reach_menu_and_issue(
    npm_digest: DigestResult,
    py_digest: DigestResult,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def candidates(*args: object) -> tuple[list[Candidate], dict[str, object]]:
        return [
            Candidate(
                "code",
                "code.example",
                "Example",
                "Example code",
                origin="licensed",
                evidence=[Evidence("src/core.ts")],
            ),
            Candidate(
                "ci",
                "ci.example",
                "CI",
                "Example CI",
                origin="licensed",
                evidence=[Evidence(".github/workflows/ci.yml")],
            ),
        ], {}

    monkeypatch.setattr("hungry_crab.compare.build_candidates", candidates)
    normal = compare_digests(
        npm_digest.out_dir, py_digest.out_dir, options=CompareOptions(maw_license="MIT")
    )
    strict = compare_digests(
        npm_digest.out_dir,
        py_digest.out_dir,
        options=CompareOptions(maw_license="MIT", mode="strict"),
    )
    assert [c.license_mode for c in normal.candidates] == ["COPY", "COPY"]
    assert {c.category: c.license_mode for c in strict.candidates} == {
        "ci": "COPY",
        "code": "REIMPLEMENT",
    }
    code = next(c for c in menu_candidates(strict.menu) if c.category == "code")
    assert "strict maw policy" in code.trace["maw_policy_reason"]
    assert code.material == "code" and strict.menu["mode"] == "strict"
    _, body = render_issue(code, strict.menu)
    assert "REIMPLEMENT" in body and "strict maw policy" in body


def test_serve_refuses_a_menu_made_before_strict_was_enabled(tmp_path: Path) -> None:
    meal = tmp_path / "meal"
    meal.mkdir()
    (meal / "menu.json").write_text('{"mode":"normal","candidates":[]}', encoding="utf-8")
    config = MawConfig(root=tmp_path, mode="strict")
    ledger = Ledger.load(None, maw="maw")
    with pytest.raises(CrabError, match="strict policy"):
        serve(meal, tmp_path, ServeOptions(), config=config, ledger=ledger)
