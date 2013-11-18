#!/bin/bash



# clean
if [ -d "./compiled_media" ]; then
rm -rf ./compiled_media
fi

# create dir
mkdir ./compiled_media

#read files of users directory

for entry in ./users/*
do
  echo "$entry"
done
