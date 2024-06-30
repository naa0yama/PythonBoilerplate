#!/usr/bin/env python3
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""test pyproject.toml."""

from pathlib import Path

from tomli import load


def test_pyproj() -> None:
    """Test if NAME matches in pyproject.toml."""
    with Path(f"{Path(__file__).parent.parent}/pyproject.toml").open("rb") as __stream:
        __config: dict = load(__stream)

    """project name."""
    assert __config["tool"]["poetry"]["name"] == __config["project"]["name"]

    """version."""
    assert __config["tool"]["poetry"]["version"] == "0.0.0"
    assert __config["project"]["version"] == "0.0.0"

    """name."""
    assert __config["tool"]["poetry"]["description"] == __config["project"]["description"]
