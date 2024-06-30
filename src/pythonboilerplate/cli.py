#!/usr/bin/env python3
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""Command line tool."""

# Standard Library
from logging import INFO
from logging import getLogger

from pythonboilerplate._version import __version__

# Third Party Library

logger = getLogger(__name__)
logger.setLevel(INFO)


# %%
def main() -> None:
    """Main function.

    Logger output version.
    """
    logger.error(__version__)


# %%
if __name__ == "__main__":
    main()
