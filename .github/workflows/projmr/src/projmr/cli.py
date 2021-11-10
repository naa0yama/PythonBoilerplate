#!/usr/bin/env python3
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""pyproject devdeps merge."""

import argparse
import json
import logging
from os import getenv
import re

from tomlkit import dumps as dumps
from tomlkit import parse as loads

logging.basicConfig(
    format="%(asctime)s %(levelname)-6s\t%(filename)-18s\t%(funcName)-12s\t%(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S%z",
    level=logging.INFO,
)


def get_args() -> argparse.Namespace:
    """Get args.

    Returns:
        dict: args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("originfile", help="please set me", type=str)
    return parser.parse_args()


# %%
def main() -> None:
    """main."""
    args = get_args()

    dict_toml_origin: dict = {}

    with open(args.originfile, "r") as f:
        dict_toml_origin = loads(f.read())
        logging.debug(json.dumps(dict_toml_origin, indent=4))

    with open(getenv("SOURCE_DIR_NAME", "failed") + "/pyproject.toml") as f:
        upstream_contents = f.read()
        dict_toml_upstream = loads(upstream_contents)

    dict_toml_origin["tool"]["poetry"].update(
        {
            "dev-dependencies": dict_toml_upstream["tool"]["poetry"]["dev-dependencies"],
        },
    )
    logging.info("merged: tool.poetry.dev-dependencies ...")

    dict_toml_origin["tool"].update(
        {
            "coverage": {"run": dict_toml_upstream["tool"]["coverage"]["run"]},
        },
    )
    logging.info("merged: tool.coverage.run ...")

    dict_toml_origin["tool"].update(
        {
            "pytest": {
                "ini_options": dict_toml_upstream["tool"]["pytest"]["ini_options"],
            },
        },
    )
    logging.info("merged: tool.pytest.ini_options ...")

    for key2 in ["black", "isort"]:
        dict_toml_origin["tool"].update({key2: dict_toml_upstream["tool"][key2]})
        logging.debug(json.dumps(dict_toml_origin, indent=4))
        logging.info("merged: " + key2 + " ...")

    logging.debug(json.dumps(dict_toml_origin, indent=4))

    with open(args.originfile, "w") as f:
        f.write(
            re.sub("(\n$)+", "\n", dumps(dict_toml_origin), flags=re.MULTILINE),
        )
    logging.info("file write.")


if __name__ == "__main__":
    main()

# %%
