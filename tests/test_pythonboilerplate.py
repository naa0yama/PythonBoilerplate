#!/usr/bin/env python3
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""pythonboilerplate."""
# Standard Library
import importlib.metadata

# First Party Library
from pythonboilerplate.cli import versions

__metadata = importlib.metadata.metadata("pythonboilerplate")


def test_versions() -> None:
    """Test version."""
    assert versions() == "{} {}".format(
        __metadata["name"],
        __metadata["version"],
    )
