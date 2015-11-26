#!/usr/bin/env bash

# db sync first
sudo apt-get update

### virtualization
# Docker
sudo apt-get install -y linux-image-extra-$(uname -r)
sudo echo aufs >> /etc/modules
sudo modprobe aufs
curl -sSL https://get.docker.com | sh

### development tools
# the essential stuff
sudo apt-get install -y build-essential

# Python
sudo apt-get install -y python-setuptools
sudo easy_install pip
sudo pip install virtualenv
