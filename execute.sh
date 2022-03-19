#!/bin/bash

SCRIPT_PATH=$(dirname "$(realpath "$0")")
source "$SCRIPT_PATH/scrapping/bin/activate"
python "$SCRIPT_PATH/actlogin.py"