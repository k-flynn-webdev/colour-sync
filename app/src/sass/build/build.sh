#!/bin/bash

## PATHS
sassDir=$(dirname $0);
dir_project=$sassDir/../../../..;

## VARS
source $dir_project/.env

export APP_NAME_FULL=$APP_NAME_FULL
export BASE_CLASS_NAME='$base-class-name'

envsubst < $sassDir/app_vars.template > $sassDir/app_vars.scss
