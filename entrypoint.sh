#!/bin/sh
set -e

if [ "$1" = 'start' ]; then

    cd ${FILEBEAT_HOME}
    ./filebeat -e -c filebeat.yml &

    cd ${APPLICATION_HOME}
    virtualenv libs
    source ./libs/Scripts/activate
    pip install -r requirements.txt
    
    while true; do
        python main.py
        sleep ${PERIOD}
    done
fi