#!/bin/bash

## onUpdate ##
## Build All Files ##

## PATHS
dir_project_build=$(dirname $0);
dir_project=$dir_project_build/..;
dir_project_api=$dir_project/api;
dir_project_app=$dir_project/app;
dir_project_static=$dir_project/static;

## VARS
NODE_ENV=production
source $dir_project/.env

## APP
cd $dir_project_app
sh ./src/sass/build/build.sh
npm run build-base-css
npm run build

## API
source `which virtualenvwrapper.sh`
workon $APP_PYTHON_ENVIROMENT

## ASSETS
cd $dir_project_api
python3 manage.py collectstatic --noinput

# ASSETS:: Copy index.html
cp $dir_project_app/dist/index.html $dir_project_static/index.html
cp $dir_project_app/dist/favicon.png $dir_project_static/favicon.png

echo "BUILD::::       $APP_NAME_FULL       PROJECT FILES REBUILT"