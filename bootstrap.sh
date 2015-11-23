#!/usr/bin/env bash

### virtualization
# Docker
sudo pacman -Sy --noconfirm docker
sudo systemctl enable docker
sudo systemctl start docker

### development tools
# the essential stuff
sudo pacman -Sy --noconfirm base-devel

# Python
sudo pacman -Sy --noconfirm python2-pip python2-virtualenv
#sudo pacman -Sy --noconfirm python-pip python-virtualenv
