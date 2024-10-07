FROM python:3.12.7-slim-bullseye

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
    apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install --no-install-recommends \
    bash \
    ca-certificates \
    curl \
    fish \
    git \
    gpg-agent \
    jq \
    nano \
    openssh-client \
    software-properties-common \
    sudo \
    wget && \
    \
    # Cleanup \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*

# Create user
RUN set -eux && \
    groupadd --gid 1000 vscode && \
    useradd -s /bin/bash --uid 1000 --gid 1000 -m vscode && \
    echo vscode:password | chpasswd && \
    passwd -d vscode && \
    echo -e "vscode\tALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/vscode

# Add Biome latest install
RUN set -eux && \
    curl -fSL -o /usr/local/bin/biome "$(curl -sfSL https://api.github.com/repos/biomejs/biome/releases/latest | \
    jq -r '.assets[] | select(.name | endswith("linux-x64")) | .browser_download_url')" && \
    chmod +x /usr/local/bin/biome && \
    type -p biome

# User lavel settings
USER vscode
ENV PATH $PATH:/home/vscode/.local/bin
RUN set -eux && \
    pip install --user "poetry==${POETRY_VERSION}" && \
    pip install --user poetry-dynamic-versioning && \
    type poetry
