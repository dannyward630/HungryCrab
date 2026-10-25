"""Every public parser surface explains its actual effect (#354)."""

import argparse

from hungry_crab.cli import build_parser


def test_public_parser_help_is_complete() -> None:
    missing: list[str] = []

    def walk(parser: argparse.ArgumentParser, path: str) -> None:
        for action in parser._actions:
            if isinstance(action, argparse._SubParsersAction):
                documented = {choice.dest for choice in action._choices_actions if choice.help}
                for name, child in action.choices.items():
                    if name not in documented:
                        missing.append(f"{path} {name}")
                    walk(child, f"{path} {name}")
            elif action.help != argparse.SUPPRESS and not action.help:
                missing.append(f"{path} {'/'.join(action.option_strings) or action.dest}")

    walk(build_parser(), "crab")
    assert missing == [], "Missing public help:\n" + "\n".join(missing)
