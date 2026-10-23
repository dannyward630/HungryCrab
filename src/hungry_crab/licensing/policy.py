"""Maw policy narrows the legal verdict; it can never grant additional permissions."""

from __future__ import annotations

from pathlib import PurePosixPath

from .matrix import Mode

_CONFIG_SUFFIXES = {".json", ".jsonc", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf"}
_CONFIG_NAMES = {
    ".editorconfig",
    ".gitignore",
    ".gitattributes",
    ".dockerignore",
    ".npmrc",
    ".yarnrc",
    ".prettierignore",
    ".prettierrc",
    ".eslintrc",
    "dockerfile",
    "makefile",
    "justfile",
    "cargo.lock",
    "poetry.lock",
    "uv.lock",
    "yarn.lock",
    "requirements.txt",
    "requirements-dev.txt",
}
_SCRIPT_CONFIG_STEMS = {
    "vitest.config",
    "vite.config",
    "jest.config",
    "eslint.config",
    "webpack.config",
    "rollup.config",
    "prettier.config",
    "tailwind.config",
    "postcss.config",
    "babel.config",
    "next.config",
    "nuxt.config",
    "svelte.config",
    "astro.config",
}
_TEMPLATE_SUFFIXES = {".md", ".markdown", ".rst", ".adoc", ".j2", ".jinja", ".jinja2", ".tmpl"}


def path_material(path: str) -> str:
    """Recognized configuration/template forms only; unknown names and scripts are code."""
    name = PurePosixPath(path).name.casefold()
    suffix = PurePosixPath(name).suffix
    if name in _CONFIG_NAMES or suffix in _CONFIG_SUFFIXES:
        return "configuration"
    if (
        suffix in {".js", ".mjs", ".cjs", ".ts", ".mts", ".cts"}
        and name.removesuffix(suffix) in _SCRIPT_CONFIG_STEMS
    ):
        return "configuration"
    if suffix in _TEMPLATE_SUFFIXES or name in {"readme", "contributing", "code_of_conduct"}:
        return "template"
    return "code"


def nutrient_material(category: str, paths: list[str]) -> str:
    """Configs/templates are the explicit exceptions. Unknown categories fail closed."""
    if category in {"code", "architecture", "history-lesson"}:
        return "code"
    if category == "issue-lesson":
        return "idea"
    if not paths or category not in {
        "ci",
        "tooling",
        "tests",
        "docs",
        "ai-config",
        "hygiene",
        "security",
        "deps",
    }:
        return "code"
    materials = {path_material(path) for path in paths}
    if "code" in materials:
        return "code"
    return "template" if "template" in materials else "configuration"


def apply_maw_policy(mode: str, *, policy: str, material: str) -> tuple[str, str]:
    if (
        policy == "strict"
        and mode in {Mode.COPY.value, Mode.COPY_FILE.value}
        and material not in {"configuration", "template"}
    ):
        return (
            Mode.REIMPLEMENT.value,
            f"strict maw policy: {mode} code requires clean-room REIMPLEMENT",
        )
    return mode, ""
