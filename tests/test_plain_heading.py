"""A heading reaches a summary as text: markup is removed, code spans and comparisons are kept."""

from __future__ import annotations

import time

import pytest

from hungry_crab.miners.wiki import plain_heading


@pytest.mark.parametrize(
    ("raw", "text"),
    [
        # This repository's own heading in docs/design/01-concept-and-skill.md.
        ("`/crab:eat <prey> [--maw .]`", "`/crab:eat <prey> [--maw .]`"),
        ("Use `Vec<T>` here", "Use `Vec<T>` here"),
        ("HashMap<K, V> and Option<T>", "HashMap&lt;K, V> and Option"),
        ("A<B, <Script>>alert(1)</Script>", "A&lt;B, alert(1)"),
        ("Map<K, <Img Src>> x", "Map&lt;K, x"),
        ("Tuple<A, <Iframe>>", "Tuple&lt;A,"),
        ("crab eat <prey> --maw <path>", "crab eat --maw"),
        ("List<String, List<Item>>", "List&lt;String, List&lt;Item>>"),
        ("See [HashMap<K, V>](https://evil.example)", "See HashMap&lt;K, V>"),
        ("See ![HashMap<K, V>](https://tracker.example/pixel)", "See"),
        ("Use <b> `Vec<T>` <i> here", "Use `Vec<T>` here"),
        ("``a ` b``", "``a ` b``"),
        ("when a <= b", "when a &lt;= b"),
        ("a < b > c", "a < b > c"),
        ('Install <img src="https://tracker.example/pixel.png">', "Install"),
        ("Usage [docs](https://evil.example/landing)", "Usage docs"),
        ("Safe <b>bold</b>", "Safe bold"),
        ("<https://evil.example>", ""),
        ("[label]: https://evil.example", "label: https://evil.example"),
        # An escaped backtick is text: what follows it is not a code span (re-review N5).
        ("Install \\`<img src=x onerror=alert(1)>`", "Install \\``"),
        ("See \\`[docs](https://evil.example)`", "See \\`docs`"),
        ("Keep \\\\`code <b>`", "Keep \\\\`code <b>`"),
    ],
)
def test_plain_heading(raw: str, text: str) -> None:
    assert plain_heading(raw) == text


def test_code_span_matching_is_linear() -> None:
    hostile = "`" + " ``" * 100_000 + "".join("`" * n + " " for n in range(1, 400))
    started = time.perf_counter()
    plain_heading(hostile)
    assert time.perf_counter() - started < 1.0


@pytest.mark.parametrize(
    "hostile",
    ["<A, " * 100_000, "<A, " * 100_000 + ">" * 100_000],
    ids=["unclosed", "nested"],
)
def test_generic_span_matching_is_linear(hostile: str) -> None:
    started = time.perf_counter()
    plain_heading(hostile)
    assert time.perf_counter() - started < 2.0
