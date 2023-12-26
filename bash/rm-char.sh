#!/bin/bash
FILES="./Series/*"
for f in $FILES
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  cat $f | tr -cd '\11\12\40-\176' > temp && mv temp $f
done
