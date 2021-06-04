#!/bin/bash
sleep 1s

script_location=$(dirname $0)
echo $script_location
cd $script_location
pwd

source ../.env
source `which virtualenvwrapper.sh`

cd ../api
pwd

workon $APP_PYTHON_ENVIROMENT
uwsgi --socket $API_IP:$API_PORT --protocol=http -w main.wsgi:application

