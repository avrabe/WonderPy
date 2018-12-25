#!/usr/bin/env bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then

    # Install some custom requirements on OS X
    # e.g. brew install pyenv-virtualenv

    case "${TOXENV}" in
        py27)
            # Install some custom Python 3.2 requirements on OS X
            ;;
    esac
else
  - rm setup.py
  - mv setup.py.travis setup.py
  - rm requirements.txt
  - mv requirements.txt.travis requirements.txt
    # Install some custom requirements on Linux
fi

python setup.py install
pip install -r requirements.txt
pip install -U pytest

which python
which pip
py.test --version
