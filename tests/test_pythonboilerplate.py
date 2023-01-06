#!/usr/bin/env python3
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""pythonboilerplate."""
# Standard Library
import importlib.metadata
from logging import ERROR

# Third Party Library
from pytest import LogCaptureFixture

# First Party Library
from pythonboilerplate.cli import main
from pythonboilerplate.cli import versions

__metadata = importlib.metadata.metadata("pythonboilerplate")


def test_versions() -> None:
    """Test version."""
    assert versions() == "{} {}".format(
        __metadata["name"],
        __metadata["version"],
    )


def test_main(caplog: LogCaptureFixture) -> None:
    """Test main."""
    main()

    assert ("pythonboilerplate.cli", ERROR, versions()) in caplog.record_tuples
