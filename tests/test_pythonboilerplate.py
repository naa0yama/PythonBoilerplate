#!/usr/bin/env python3
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""pythonboilerplate."""

from logging import ERROR

import pytest
from pythonboilerplate.cli import main
import setuptools_git_versioning


def test_main(caplog: pytest.LogCaptureFixture) -> None:
    """Test main."""
    main()

    assert (
        "pythonboilerplate.cli",
        ERROR,
        f"{setuptools_git_versioning.get_version()}",
    ) in caplog.record_tuples
