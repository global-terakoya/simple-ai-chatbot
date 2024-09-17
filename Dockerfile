FROM ubuntu:24.04

ARG USERNAME=devuser
ARG USER_UID=${USER_UID}
ARG GROUPNAME=ubuntu
ARG USER_GID=1000

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    wget \
    git \
    build-essential \
    python3 \
    python3-pip \
    gnupg \
    software-properties-common \
    zip \
    unzip \
    vim \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y ca-certificates curl \
    && install -m 0755 -d /etc/apt/keyrings \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc \
    && chmod a+r /etc/apt/keyrings/docker.asc \
    && echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && apt-get update \
    && apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin \
    && rm -rf /var/lib/apt/lists/*

RUN curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/nektos/act/master/install.sh | bash

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt --no-cache-dir --break-system-packages \
    && rm -f /tmp/requirements.txt

WORKDIR /workspace

RUN useradd -l -m -d /home/${USERNAME} -s /bin/bash ${USERNAME} --uid ${USER_UID} --gid ${USER_GID} \
    && apt-get update \
    && apt-get install --no-install-recommends -y sudo \
    && rm -rf /var/lib/apt/lists/* \
    && echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME} \
    && usermod -aG sudo ${USERNAME} \
    && usermod -aG docker ${USERNAME} \
    && chown -R ${USERNAME}:${GROUPNAME} /workspace

USER ${USERNAME}

ENV PYTHONPATH=/workspaces/simple-ai-chatbot/src:/workspaces/simple-ai-chatbot/tests:${PYTHONPATH}