#!/bin/bash

OLD_TAG_O="<p>";
OLD_TAG_C="</p>";
NEW_TAG_O="<tag>";
NEW_TAG_C="</tag>";

DEF_PATH="h5482.novius.net";

if [ -z $1 ]; then
echo "enter a user id as first argument"
exit 0
else
id=$1
fi


#echo -n "enter user id > "
#read id
echo -en "fetching tags from : $id \n"
wget -N --cookie=on --load-cookies ./cookies.txt --directory-prefix=./users/$id http://$DEF_PATH/admin/promenade/utilisateur/crud/insert_update/$id
if [ -f "./users/$id/$id" ]; then
echo "<tags>" > ./users/$id/tags.xml
cat ./users/$id/$id | grep Réponse | sed -e 's/<p>Réponse : /<tag>/g;s/<\/p>/<\/tag>/g' >> ./users/$id/tags.xml
echo "</tags>" >> ./users/$id/tags.xml
else
echo -e "\n\n F I L E    D O E S N T     E X I S T  \n\n"
fi
