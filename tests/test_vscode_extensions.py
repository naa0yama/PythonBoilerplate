#!/usr/bin/env python3
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""test_vscode_extensions."""

# Standard Library
import json
from pathlib import Path
import re


# %%
def load_jsonc(filepath: str, encoding: str = "utf-8") -> dict:
    """Load jsonc."""
    with Path(filepath, encoding=encoding).open("wb") as f:
        text = f.read()
    text_without_comment = re.sub(r"/\*[\s\S]*?\*/|//.*", "", text)
    json_obj: dict = json.loads(text_without_comment)
    return json_obj


# %%
def test_vscode_extensions_sync() -> None:
    """Test vscode extensions sync."""
    __vscode_dcit = load_jsonc(
        filepath=Path(__file__).parent / ".vscode/extensions.json",
    )

    __devcontainer_dcit = load_jsonc(
        filepath=Path(__file__).parent / ".devcontainer/devcontainer.json",
    )

    assert (
        __vscode_dcit["recommendations"]
        == __devcontainer_dcit["customizations"]["vscode"]["extensions"]
    )


# %%
