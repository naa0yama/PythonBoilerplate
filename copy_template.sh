#!/usr/bin/env bash

set -eu

#- -----------------------------------------------------------------------------
#- script_name
#-
#- -----------------------------------------------------------------------------

CURRENT_DIR="$(dirname "${0}")"

if [ -z "${1}" ]; then
  echo "destnation dir not found."
  exit 1
fi

DESTNATION_DIR="$(dirname "${1}")"

SYNC_FILES=(
  '.github'
  '.vscode'
  '.gitignore'
  'src'
  'tests'
  'LICENSE'
  'pyproject.toml'
  'setup.cfg'
  'tox.ini'
)

for file in "${SYNC_FILES[@]}"
do
  cp -av ${CURRENT_DIR}/${file} ${DESTNATION_DIR}
done
