#!/bin/sh

cd $(dirname "$0")/..

default_mod=main
fixtures_dir=./$default_mod/fixtures
mkdir -p $fixtures_dir

dumpdata() {
    obj=$1
    test "$2" && mod=$2 || mod=$default_mod
    test "$3" && file=$3 || file=$fixtures_dir/$obj.json
    python manage.py dumpdata $mod.$obj --indent 4 > $file && echo Dumped to $file
}

dumpdata Hacker
dumpdata OneLiner

# eof