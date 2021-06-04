#!/bin/bash
sleep 1s

script_location=$(dirname $0)
echo $script_location/..
cd $script_location/..
pwd

source .env
source `which virtualenvwrapper.sh`

workon $APP_PYTHON_ENVIROMENT
python3 "api/manage.py" runserver --nostatic "$API_IP:$API_PORT"

