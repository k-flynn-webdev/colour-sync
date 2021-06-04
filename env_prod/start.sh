#!/bin/bash

## PATHS
dir_project_production=$(dirname $0);
dir_project=$dir_project_production/..;

## VARS
source $dir_project/.env

# Add App to PM2 processes
pm2 start ./run_api_production.sh --name "${APP_NAME_FULL}-app"

# Add Auto-Build to PM2 processes - based on a timed git HEAD diff
cd ../builder;
pm2 start npm --name "${APP_NAME_FULL}-builder" -- start
