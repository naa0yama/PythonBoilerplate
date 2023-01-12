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
import setuptools_git_versioning

# First Party Library
from pythonboilerplate.cli import main

__metadata = importlib.metadata.metadata("pythonboilerplate")


def test_main(caplog: LogCaptureFixture) -> None:
    """Test main."""
    main()

    assert (
        "pythonboilerplate.cli",
        ERROR,
        "{}".format(setuptools_git_versioning.get_version()),
    ) in caplog.record_tuples
