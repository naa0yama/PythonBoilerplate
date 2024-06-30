# pythonboilerplate

[![codecov](https://codecov.io/gh/naa0yama/pythonboilerplate/branch/main/graph/badge.svg?token=D8YU7EYIYZ)](https://codecov.io/gh/naa0yama/pythonboilerplate)

Python で開発する時用ボイラープレート

## チュートリアル

[VSCode で極力手を抜いて開発するハンドブック](https://zenn.dev/naa0yama/books/python-boilerplate) を書きました

## Git タグを利用した 動的 Version 付け

GitHub で管理すると tag を付けたらそのバージョンでリリースしたくなる。  
が、通常の方法では `pyproject.toml` の複数 version 箇所を書き換える必要が出る。  
これを回避するため、[mtkennerly/poetry-dynamic-versioning](https://github.com/mtkennerly/poetry-dynamic-versioning) を利用する。

本レポジトリーの `.devcontainer/Dockerfile` には組み込み済みだが、手動でやる場合は下記のようにする  

```bash
# pip の場合
pip install --user poetry-dynamic-versioning

# asdf の場合
poetry self add "poetry-dynamic-versioning[plugin]"

```

どちらも正しく導入出来ると下記のように `poetry self show plugins` で確認出来る

```bash
> poetry self show plugins

  - poetry-dynamic-versioning (1.4.0) Plugin for Poetry to enable dynamic versioning based on VCS tags
      1 application plugin

      Dependencies
        - dunamai (>=1.21.0,<2.0.0)
        - jinja2 (>=2.11.1,<4)
        - poetry (>=1.2.0,<2.0.0)
        - tomlkit (>=0.4)

  - poetry-plugin-export (1.8.0) Poetry plugin to export the dependencies to various formats
      1 application plugin

      Dependencies
        - poetry (>=1.8.0,<3.0.0)
        - poetry-core (>=1.7.0,<3.0.0)

```

## Memo

* 2024-05-09
  * Ruff
    * Linter
    * Formatter
  * Type Checker
    * mypy

* 2024-04-12
  * Linter
    * Markdown
      * Markdown All in One
    * Python
      * Black
      * Python Test Explorer for Visual Studio Code
      * Flake8
      * isort
      * Mypy Type Checker
      * Python
      * Pylance
      * Jupyter
      * autoDocstring
      * Coverage Gutters
    * Json
      * Prettier - Code formatter
    * Yaml
      * YAML
