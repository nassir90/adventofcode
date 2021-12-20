#!/bin/bash

file=`mydate.sh`
python3 1.py $1 > $file
grep '^\[' $file | sort | uniq | wc -l
