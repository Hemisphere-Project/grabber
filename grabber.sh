#!/bin/bash

DEF_PATH="h5482.novius.net";

if [ -z $1 ]; then
echo "enter a user id as first argument"
exit 0
else
id=$1
fi

#echo -n "enter user id > "
#read id
echo -en "fetching media from : $id \n"
wget -r -A jpeg,jpg,bmp,gif,png,wav,3ga,3gpp,mp3,m4a --cookie=on --load-cookies ./cookies.txt --directory-prefix=./users/$id http://$DEF_PATH/admin/promenade/utilisateur/crud/insert_update/$id
if [ -d "./users/$id/$DEF_PATH/data" ]; then
mv ./users/$id/h5482.novius.net/data ./users/$id/
rm -rf ./users/$id/$DEF_PATH/
else
echo -e "\n\n D A T A    D O E S N T     E X I S T  \n\n"
rm -rf ./users/$id
fi
