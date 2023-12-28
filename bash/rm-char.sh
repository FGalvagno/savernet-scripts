#!/bin/bash
FILES="./Series/*"
for f in $FILES
do
  echo "Processing $f file..."
  cat $f | tr -cd '\11\12\40-\176' > temp && mv temp $f
done
