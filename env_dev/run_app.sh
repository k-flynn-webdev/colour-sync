#!/bin/bash
sleep 1s

script_location=$(dirname $0)
source $script_location/../.env

echo $script_location/..
cd $script_location/../app
pwd

npm run serve -- --port $APP_PORT --host $APP_IP

