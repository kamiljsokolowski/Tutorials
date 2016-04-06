#!/usr/bin/env bash

# Python
sudo apt-get update -q && sudo apt-get install -y \
    python-setuptools \
 && sudo easy_install pip \
 && sudo pip install virtualenv \
 && sudo pip install virtualenvwrapper

