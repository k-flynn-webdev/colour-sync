#!/bin/bash

## PATHS
dir_project_production=$(dirname $0);
dir_project=$dir_project_production/..;

## VARS
source $dir_project/.env

mysqldump -u $DATABASE_USER -h 127.0.0.1 -p $DATABASE_PASS $DATABASE_NAME | gzip -9 > minitrack_$(date +%y%m%d)_DB.gz