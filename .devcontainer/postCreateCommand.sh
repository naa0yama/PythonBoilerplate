#/bin/bash
set -eux

rm -rf .venv/
poetry install --no-interaction
