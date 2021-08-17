#!/bin/bash

## PATHS
dir_project_production=$(dirname $0);
dir_project=$dir_project_production/..;

## VARS
source $dir_project/.env

## Create css files dir
mkdir -p $dir_project/static/$APP_NAME_SHORT
