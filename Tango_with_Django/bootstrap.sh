#!/usr/bin/env bash

# Python
sudo apt-get update -q && sudo apt-get install -y \
    python-dev \
    python-setuptools \
    libjpeg8-dev \
    zlib1g-dev \
 && sudo easy_install pip \
 && sudo pip install virtualenv \
 && sudo pip install virtualenvwrapper

