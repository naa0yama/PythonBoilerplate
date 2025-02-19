FROM python:3.12.8-slim-bookworm

ARG PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

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
    groupadd --gid 60001 vscode && \
    useradd -s /bin/bash --uid 60001 --gid 60001 -m vscode && \
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
COPY --chown=vscode --chmod=644 .tool-versions /tmp/.tool-versions
ENV PATH=$PATH:/home/vscode/.local/bin
RUN set -eux && \
    pip install --user "poetry==$(grep -oP '(?<=poetry\s).+' /tmp/.tool-versions)" && \
    pip install --user poetry-dynamic-versioning && \
    type poetry && \
    rm -f /tmp/.tool-versions
