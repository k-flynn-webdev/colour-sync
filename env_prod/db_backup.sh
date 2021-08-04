#!/bin/bash

## PATHS
dir_project_production=$(dirname $0);
dir_project=$dir_project_production/..;

## VARS
source $dir_project/.env

mysqldump -u $DATABASE_USER -h 127.0.0.1 -p $DATABASE_NAME | gzip -9 > ../../$APP_NAME_SHORT$(date +_%y_%m_%d)_DB.gz