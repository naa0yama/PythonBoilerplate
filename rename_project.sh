#!/usr/bin/env bash
set -eu

read -p "Renmae project name          :" INPUT_PROJ
read -p "Renmae project description   :" INPUT_DESC
echo "+-------------------------------------------------------+"
echo "Project name           $INPUT_PROJ"
echo "Project description    $INPUT_DESC"
echo "+-------------------------------------------------------+"
read -p " Conform ? (y/n): " CHECK_YN

case "$CHECK_YN" in
  [yY])
    set -x
    sed -i'' -e "s/pythonboilerplate/${INPUT_PROJ}/g"                     pyproject.toml
    sed -i'' -e "s/Python を開発する時用ボイラープレート/${INPUT_DESC}/g" pyproject.toml
    sed -i'' -e "s/# pythonboilerplate/# ${INPUT_PROJ}/g"                 README.md
    sed -i'' -e "s/pythonboilerplate/${INPUT_PROJ}/g"                     .vscode/settings.json
    sed -i'' -e "s/pythonboilerplate/${INPUT_PROJ}/g"                     src/pythonboilerplate/__init__.py
    sed -i'' -e "s/pythonboilerplate/${INPUT_PROJ}/g"                     tests/test_pythonboilerplate.py
    mv src/pythonboilerplate              src/${INPUT_PROJ}
    mv tests/test_pythonboilerplate.py    tests/test_${INPUT_PROJ}.py
    set +x
    echo "+-------------------------------------------------------+"
    echo "Completed."
    echo "+-------------------------------------------------------+"
    exit 0
    ;;
  [nN]) echo "canceled."
    exit 1
    ;;
esac
