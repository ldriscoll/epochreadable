#!/bin/bash

# Exit if something fails
set -e

if [[ -z "$XDG_DATA_HOME" ]]; then
    prefix=~/.local/share
else
    prefix="$XDG_DATA_HOME"
fi

rm $prefix/kservices5/krunner/dbusplugins/plasma-runner-epochreadable.desktop
rm $prefix/dbus-1/services/org.kde.epochreadable.service
kquitapp5 krunner

