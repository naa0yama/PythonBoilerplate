#!/usr/bin/env python3
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""pythonboilerplate."""

from logging import ERROR

import pytest

from pythonboilerplate._version import __version__
from pythonboilerplate.cli import main


def test_main(caplog: pytest.LogCaptureFixture) -> None:
    """Test main."""
    main()

    assert (
        "pythonboilerplate.cli",
        ERROR,
        f"{__version__}",
    ) in caplog.record_tuples
