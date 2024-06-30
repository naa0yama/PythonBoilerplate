#!/usr/bin/env python3
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""conf."""

# Standard Library
from pathlib import Path
import sys

# Third Party Library
from sphinx_pyproject import SphinxConfig

sys.path.append(f"{Path(__file__).parent.parent}")

config = SphinxConfig(
    f"{Path(__file__).parent.parent}/pyproject.toml",
    globalns=globals(),
    style="poetry",
)
