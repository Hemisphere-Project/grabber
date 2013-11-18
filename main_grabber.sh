#!/bin/bash


if [ -z $1 ]; then
echo "enter a user id as first argument"
exit 0
else
id=$1
fi

# clean
if [ -d "./users/$id" ]; then
rm -rf ./users/$id
fi

echo -en "\n\n GRAB \n\n"
bash grabber.sh $id
echo -en "\n\n TAG GRAB \n\n"
bash tag_grabber.sh $id
echo -en "\n\n RENAME MEDIA FOLDERS \n\n"
python rename_media_folder.py $id
echo -en "\n\n\n\n JOB's DONE ;) \n\n\n\n"
