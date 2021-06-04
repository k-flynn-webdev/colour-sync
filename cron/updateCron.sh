#!/bin/bash

GIT_BRANCH_NAME="main"

### A LAZY DELAYED CI/CD APPROACH
### A SIMPLE
###           GIT CHECK
###           TIME DELAY CHECK
###           GIT PULL BASH SCRIPT
### USE TO KEEP A BRANCH UPTO DATE WITH ITS REMOTE COUNTERPART
script_location=$(dirname $0)
cd $script_location
pwd

DELAY=3600
GIT_URL=`git remote get-url origin`

git fetch

GIT_LOCAL=`git show --no-notes --format=format:"%H" $GIT_BRANCH_NAME | head -n 1`
GIT_REMOTE=`git show --no-notes --format=format:"%H" origin/$GIT_BRANCH_NAME | head -n 1`

TIME_CURRENT=`date "+%s"`
TIME_LAST_COMMIT=`git show -s --format=%ct $GIT_REMOTE`
TIME_DIFF="$(($TIME_CURRENT - $TIME_LAST_COMMIT))"

if [ $GIT_REMOTE != $GIT_LOCAL ] && [ "$TIME_DIFF" -gt "$DELAY" ]; then
  echo "[ $GIT_URL :: $GIT_BRANCH_NAME ] Updated"
  git pull --no-edit

#  if [ -f "./updateTrigger.sh" ]; then
#     ./updateTrigger.sh
#  fi

fi
