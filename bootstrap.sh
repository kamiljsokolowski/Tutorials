#!/usr/bin/env bash

sudo apt-get update -q && sudo apt-get install -y \
    linux-image-extra-$(uname -r) \
    build-essential \
    python-setuptools \
    python3-setuptools

### virtualization
# Docker
bash <<EODOCKER
sudo echo aufs >> /etc/modules
sudo modprobe aufs
curl -sSL https://get.docker.com | sh
EODOCKER

### develop
# Python2
bash <<EOPYTHON
sudo easy_install pip
EOPYTHON
# Python3
bash <<EOPYTHON3
sudo easy_install3 pip
sudo pip install virtualenv
EOPYTHON3

