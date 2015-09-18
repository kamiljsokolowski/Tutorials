#!/usr/bin/env bash

# dotfiles
mv .vimrc .vimrc.terry
mkdir .dotfiles
cd .dotfiles
git clone https://github.com/sokolowskik/dotfiles.git .
chmod +x bootstrap.sh
./bootstrap.sh

### development tools
# the essential stuff
sudo pacman -Sy --noconfirm base-devel

# Python
sudo pacman -Sy --noconfirm python2-pip python2-virtualenv
#sudo pacman -Sy --noconfirm python-pip python-virtualenv
