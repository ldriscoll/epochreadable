#!/bin/bash

# Exit if something fails
set -e


if [[ -z "$XDG_DATA_HOME" ]]; then
    prefix=~/.local/share
else
    prefix="$XDG_DATA_HOME"
fi

mkdir -p $prefix/kservices5/krunner/dbusplugins/
mkdir -p $prefix/dbus-1/services/

cp plasma-runner-unixtime.desktop $prefix/kservices5/krunner/dbusplugins/
sed "s|/home/luke/projects/unixtime/unixtime.py|${PWD}/unixtime.py|" "org.kde.unixtime.service" > $prefix/dbus-1/services/org.kde.unixtime.service

kquitapp5 krunner

