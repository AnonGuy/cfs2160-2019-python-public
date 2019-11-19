#! /usr/bin/env bash

for name in 'python3.8' 'python3' 'python'
do
  location="$(which $name 2>/dev/null)"
  if [[ ! -z $location ]]
  then
    break
  fi
done

echo "Python interpreter location: $location" >&2
echo >&2

if [[ ! "$($location -V)" =~ .*3.8.* ]]
then
  echo "ERROR: Python version 3.8+ is required to run this submission."
  exit 1
fi

$location -m speed_camera
