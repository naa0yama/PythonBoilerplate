#!/usr/bin/env python3
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""cli."""
# Standard Library
import importlib.metadata
from logging import INFO
from logging import getLogger
from os import path

logger = getLogger(__name__)
logger.setLevel(INFO)


# %%
def versions() -> str:
    """Versions."""
    __metadata = importlib.metadata.metadata(path.basename(path.dirname(__file__)))

    versions: str = "{} {}".format(
        __metadata["name"],
        __metadata["version"],
    )

    return versions


def main() -> None:
    """Main."""
    logger.error(versions())


# %%
if __name__ == "__main__":
    main()
