#!/bin/bash

SCRIPT_PATH=$(dirname "$(realpath "$0")")
source "$SCRIPT_PATH/scrapping/bin/activate"
python "$SCRIPT_PATH/actlogin.py"

# ln -s ~/Projects/scrapping-stuff/ /usr/local/lib/actlogin
# ln -s “$(pwd)/actlogin.service” /etc/systemd/system/actlogin.service
