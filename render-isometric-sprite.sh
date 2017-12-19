#!/bin/sh

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")

if [ "$1" = "" ]
then
  echo "Usage: `basename $0` myfile.blend [--scale 100] [--dest /path/to/dir]"
else
  blend_file="$1"; shift
  blender ${blend_file} --background --python "$SCRIPTPATH/render.py" "$@"
fi
