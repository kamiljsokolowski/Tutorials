#!/usr/bin/env bash

sudo apt-get update -q && sudo apt-get install -y \
    linux-image-extra-$(uname -r) \
    build-essential \
    python-setuptools

### virtualization
# Docker
bash <<EODOCKER
sudo echo aufs >> /etc/modules
sudo modprobe aufs
curl -sSL https://get.docker.com | sh
EODOCKER

### develop
# Python
bash <<EOPYTHON
sudo easy_install pip
sudo pip install virtualenv
EOPYTHON

