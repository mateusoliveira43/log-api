#!/bin/bash

ROOT="$(dirname $( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P ))"
FILE="$ROOT/.env"
USER_NAME='developer'
PROJECT_NAME='log-api'

if ! test -f $FILE; then
    echo "USER_ID=$(id -u)" >> $FILE
    echo "GROUP_ID=$(id -g)" >> $FILE
    echo "USER_NAME=$USER_NAME" >> $FILE
    echo "PROJECT_NAME=$PROJECT_NAME" >> $FILE
    echo "WORK_DIR=/home/$USER_NAME/$PROJECT_NAME" >> $FILE
    # TODO add service variables (HOST, PORT, etc)
    echo ".env file created in project's root"
fi
