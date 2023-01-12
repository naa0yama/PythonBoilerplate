#!/usr/bin/env python3
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""cli."""
# Standard Library
from logging import INFO
from logging import getLogger

# Third Party Library
import setuptools_git_versioning

logger = getLogger(__name__)
logger.setLevel(INFO)


# %%
def main() -> None:
    """Main."""
    logger.error(setuptools_git_versioning.get_version())


# %%
if __name__ == "__main__":
    main()
