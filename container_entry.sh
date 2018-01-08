#!/bin/bash
set -eux
printenv
cd /opt/ducky
# source venv/bin/activate

flask run --host=0.0.0.0
