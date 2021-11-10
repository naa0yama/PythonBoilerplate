# pythonboilerplate

[![codecov](https://codecov.io/gh/naa0yama/pythonboilerplate/branch/main/graph/badge.svg?token=D8YU7EYIYZ)](https://codecov.io/gh/naa0yama/pythonboilerplate)

Python で開発する時用ボイラープレート

## TOC

- [pythonboilerplate](#pythonboilerplate)
  - [TOC](#toc)
  - [pyenv インストール](#pyenv-インストール)
  - [poetry](#poetry)
    - [インストール](#インストール)
    - [設定](#設定)
    - [使いそうなコマンド](#使いそうなコマンド)
      - [Poetryのアップデート](#poetryのアップデート)
      - [プロジェクトの作成](#プロジェクトの作成)
      - [パッケージのインストール](#パッケージのインストール)
      - [パッケージのアンインストール](#パッケージのアンインストール)
      - [パッケージ一覧を表示](#パッケージ一覧を表示)
      - [仮想環境内でのコマンドの実行](#仮想環境内でのコマンドの実行)
      - [仮想環境内でシェルを立ち上げる](#仮想環境内でシェルを立ち上げる)
  - [Pythonのバージョンの管理](#pythonのバージョンの管理)
  - [VSCode](#vscode)
    - [設定](#設定-1)


## pyenv インストール

* [pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv)


## poetry

### インストール

* [python\-poetry/poetry: Python dependency management and packaging made easy\.](https://github.com/python-poetry/poetry#installation)


### 設定

* プロジェクト内に venv が作成されないと VSCode などで利用するには都合が悪いため、 poetry のでデフォルト設定を変更します

```shell
poetry config virtualenvs.in-project true

```

### 使いそうなコマンド

---

#### Poetryのアップデート

```shell
poetry self update

```

#### プロジェクトの作成

```shell
poetry new <project-name>

```

#### パッケージのインストール

```shell
poetry add <package-name>

```

#### パッケージのアンインストール

```shell
poetry remove <package-name>

```

#### パッケージ一覧を表示

```shell
poetry show

```

#### 仮想環境内でのコマンドの実行

```shell
poetry run <commands...>

```

`python`でファイルを実行

```shell
poetry run python <file-name>

```

#### 仮想環境内でシェルを立ち上げる

仮想環境内でシェルを立ち上げます

```bash
poetry shell

```

## Pythonのバージョンの管理

`pyenv` を併用して行う方法です

Python 3.8.6 を例とします

まず `pyenv` で 3.8.6 がインストールされていなければインストールします

```shell
pyenv install 3.8.6

```

プロジェクト内のローカルのバージョンを変更します

```shell
pyenv local 3.8.6

```

コマンドで仮想環境を構築します

```shell
poetry env use 3.8.6

```

これでプロジェクト内の Python のバージョンは 3.8.6 になります

## VSCode
### 設定
