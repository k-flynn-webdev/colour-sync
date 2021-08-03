#!/bin/bash

## PATHS
dir_project_production=$(dirname $0);
dir_project=$dir_project_production/..;

## VARS
source $dir_project/.env

mysqldump -u $DATABASE_USER -p $DATABASE_PASS $DATABASE_NAME | gzip -9 > $(date +%y%m%d)_dbBackUpsql.gz
