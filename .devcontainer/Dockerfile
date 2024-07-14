FROM python:3.10.14-slim-bullseye

ARG PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    \
    POETRY_VERSION=1.8.2

ENV TZ=Asia/Tokyo

SHELL [ "/bin/bash", "-c" ]

# set Timezone
RUN set -eux && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN set -eux && \
    apt -y update && \
    apt -y upgrade && \
    apt -y install --no-install-recommends \
    bash \
    ca-certificates \
    curl \
    fish \
    git \
    gpg-agent \
    nano \
    openssh-client \
    software-properties-common \
    sudo \
    wget && \
    \
    # Cleanup \
    apt -y autoremove && \
    apt -y clean && \
    rm -rf /var/lib/apt/lists/*

# Create user
RUN set -eux && \
    groupadd --gid 1000 vscode && \
    useradd -s /bin/bash --uid 1000 --gid 1000 -m vscode && \
    echo vscode:password | chpasswd && \
    passwd -d vscode && \
    echo -e "vscode\tALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/vscode

# User lavel settings
USER vscode
ENV PATH $PATH:/home/vscode/.local/bin
RUN set -eux && \
    pip install --user "poetry==${POETRY_VERSION}" && \
    pip install --user poetry-dynamic-versioning && \
    type poetry
