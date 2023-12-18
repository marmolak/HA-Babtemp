#!/usr/bin/env bash
# Say current temperature on macOS.


 source ./venv/bin/activate

 declare -r TEMPERATURE=$(python3 contrib/get-temp-from-ha-test.py)

 say "${TEMPERATURE}"

