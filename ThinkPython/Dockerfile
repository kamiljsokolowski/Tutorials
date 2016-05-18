# ThinkPython
# ver 0.1

FROM ubuntu:14.04
RUN apt-get -q update && apt-get install -y \
    python-setuptools \
    python3-setuptools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && easy_install pip \
    && easy_install3 pip \
    && pip install virtualenv

