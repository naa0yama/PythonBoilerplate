FROM python:3.10.14-slim-bullseye
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.2

RUN \
    set -eux \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    \
    && apt-get update \
    && apt-get -y install \
    fish \
    curl \
    git \
    \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install "poetry==$POETRY_VERSION"

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=1000
RUN \
    set -eux \
    && groupadd --gid $USER_GID $USERNAME \
    && useradd -s /usr/bin/fish --uid $USER_UID --gid $USER_GID -m $USERNAME

USER $USERNAME

RUN \
    set -eux \
    && /usr/bin/fish -c 'curl -sL https://git.io/fisher | source && fisher install jorgebucaran/fisher' \
    && /usr/bin/fish -c 'fisher install oh-my-fish/theme-bobthefish'
