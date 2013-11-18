#!/bin/bash

OF="users/tags_c.xml"

echo "<tags>" > ./$OF
cat `find ./ -iname "tags.xml" -print` | grep '<tag>' >> ./$OF
echo "</tags>" >> ./$OF
