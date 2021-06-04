#!/bin/bash

## PATHS
nginx=$(dirname $0);
dir_project=$nginx/..;

## VARS
source $dir_project/.env

export URL_WEB=$URL_WEB
export APP_NAME_SHORT=$APP_NAME_SHORT
export APP_NAME_FULL=$APP_NAME_FULL
export API_ADDRESS=$API_ADDRESS

envsubst < $nginx/nginx.template > $URL_WEB
