#!/bin/sh

author=""
description=""
stdLib="eslint"
while [ $# -gt 0 ] 
do
    case "$1" in
        --author)
            export author=$2
            shift 2;;
        --description)
            export description=$2
            shift 2;;
        *)
    continue
    esac
done

echo "Setting Up NodeJS Project"
echo "===================="

if [ "$author" == "" ] 
then
    read -p "Author Name: " author
else
    echo "Author Name: $author"
fi

if [ "$description" == "" ] 
then
    read -p "Description: " description
else
    echo "Description: $description"
fi


npm init -y > /dev/null
sed -i "s/\"description\": \"\",/\"description\": \"$description\",/" package.json
sed -i "s/\"author\": \"\",/\"author\": \"$author\",/" package.json

read -p "Libraries: " libraries
IFS=" "
read -ra arr <<< "$libraries"

npm i $stdLib
for val in "${arr[@]}"
do
    npm i $val
done


clear
echo "Finished Setting Up NodeJS Project"
echo "===================="
echo "Author: $author"
echo "Description: $description"
echo "Libraries: $stdLib $libraries"
