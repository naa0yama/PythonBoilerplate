# pythonboilerplate

[![codecov](https://codecov.io/gh/naa0yama/pythonboilerplate/branch/main/graph/badge.svg?token=D8YU7EYIYZ)](https://codecov.io/gh/naa0yama/pythonboilerplate)

Python で開発する時用ボイラープレート

## TOC

- [pythonboilerplate](#pythonboilerplate)
  - [TOC](#toc)
  - [asdf のインストール](#asdf-のインストール)
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

## asdf のインストール

* [Getting Started \| asdf](https://asdf-vm.com/guide/getting-started.html#_1-install-dependencies)

asdf をインストールします。

* Python の依存関係を追加する
  * Ref: [Home · pyenv/pyenv Wiki](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)

```bash
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

```

* Python のプラグインを追加

```bash
asdf plugin-add python

```

* Python のバージョンを追加

```bash
asdf install python 3.8.13

```

* Python のバージョンを Global バージョンへ設定


```bash
asdf global python 3.8.13

```

* プロジェクトの Python バージョンを指定する場合

プロジェクト直下のディレクトリーに移動し下記を実行します。

```bash
asdf local python 3.8.13

```

これでプロジェクト内の Python のバージョンは 3.8.13 になります


## poetry

### インストール

Ref: [asdf\-community/asdf\-poetry: Poetry plugin for the asdf version manager](https://github.com/asdf-community/asdf-poetry)

poetry のインストールを直で実施すると virtualenv を作成したときに global の python バージョンで作成
されてしまうため asdf を利用して poetry をインストールする

```bash
asdf plugin add poetry
asdf install poetry latest
asdf global poetry <インストールされたバージョン>

```


* poetry の 補完設定

Ref: [Introduction \| Documentation \| Poetry \- Python dependency management and packaging made easy](https://python-poetry.org/docs/#enable-tab-completion-for-bash-fish-or-zsh)

```bash
# Fish (Homebrew)
poetry completions fish > (brew --prefix)/share/fish/vendor_completions.d/poetry.fish

```


### 設定

* ~~プロジェクト内に venv が作成されないと VSCode などで利用するには都合が悪いため、 poetry のでデフォルト設定を変更します~~

2022/06/17 にリリースされたバージョンで `python.pythonPath` などが非推奨となったため poetry で自動生成される venv を使うため、設定を削除

` poetry config --list` を実行して `virtualenvs.in-project` が `true` の場合 は下記を実行してください

```shell
poetry config virtualenvs.in-project false

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
