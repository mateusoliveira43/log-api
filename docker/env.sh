#!/bin/bash

ROOT="$(dirname $( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P ))"
FILE="$ROOT/.env"
USER_NAME='developer'

if ! test -f $FILE; then
    echo "USER_ID=$(id -u)" >> $FILE
    echo "GROUP_ID=$(id -g)" >> $FILE
    echo "USER_NAME=$USER_NAME" >> $FILE
    echo "WORK_DIR=/home/$USER_NAME/log-api" >> $FILE
    echo "TOKEN_SECRET_KEY=$(openssl rand -hex 32)" >> $FILE
    echo "TOKEN_ALGORITHM=HS256" >> $FILE
    echo "API_HOST=0.0.0.0" >> $FILE
    echo "API_PORT=3000" >> $FILE
    echo "DATABASE_HOST=log-database" >> $FILE
    echo "DATABASE_PORT=5432" >> $FILE
    echo ".env file created in project's root"
fi
