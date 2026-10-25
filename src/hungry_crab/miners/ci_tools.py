"""Shared CI tool classifications for mining, traits and source evidence."""

TEST_TOOLS = frozenset(
    {
        "pytest",
        "unittest",
        "vitest",
        "jest",
        "mocha",
        "playwright",
        "cypress",
        "npm test",
        "dotnet test",
        "cargo test",
        "go test",
        "tox",
        "nox",
        "make test",
        "just test",
        "task test",
        "cargo nextest",
        "rake test",
    }
)
LINT_TOOLS = frozenset(
    {
        "ruff",
        "black",
        "flake8",
        "isort",
        "mypy",
        "pyright",
        "eslint",
        "prettier",
        "biome",
        "tsc",
        "dotnet format",
        "cargo clippy",
        "cargo fmt",
        "go vet",
        "golangci-lint",
        "markdownlint",
        "shellcheck",
        "actionlint",
        "pre-commit",
        "make lint",
        "just lint",
        "task lint",
        "make check",
        "just check",
        "task check",
    }
)
