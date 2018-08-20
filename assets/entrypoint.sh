#!/bin/bash

PROJECT_NAME={{.Title}}
PARENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

exec gunicorn \
    --name ${PROJECT_NAME} \
    --config "${PARENT_DIR}/../conf/gunicorn-config.py" \
    --log-config "${PARENT_DIR}/../conf/gunicorn-logging.conf" \
    "bin.main:wsgi()"
