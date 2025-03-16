#!/usr/bin/env python3
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""Command line tool."""

from logging import INFO
from logging import StreamHandler
from logging import getLogger

from pythonboilerplate._version import __version__

logger = getLogger(__name__)
logger.setLevel(INFO)

handler = StreamHandler()
handler.setLevel(INFO)
logger.addHandler(handler)


def main() -> None:
    """Main function.

    Logger output version.
    """
    logger.info(__version__)


if __name__ == "__main__":  # pragma: no cover
    main()
