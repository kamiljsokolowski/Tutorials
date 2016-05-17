#!/usr/bin/env bash

# Docker
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
sudo add-apt-repository "deb https://apt.dockerproject.org/repo ubuntu-trusty main"
sudo apt-get update -q && sudo apt-get install -y \
    linux-image-extra-$(uname -r) \
    build-essential \
    apt-transport-https \
    ca-certificates \
    docker-engine

echo "aufs" |sudo tee -a /etc/modules
sudo modprobe aufs

