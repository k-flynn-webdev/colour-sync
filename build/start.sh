#!/bin/bash

## PATHS
dir_project_build=$(dirname $0);
dir_project=$dir_project_build/..;

## VARS
source $dir_project/.env

# Add Build Watcher to PM2 processes
pm2 start npm --name "${APP_NAME_FULL}-build" -- start
