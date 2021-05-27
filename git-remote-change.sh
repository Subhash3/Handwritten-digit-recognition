#!/bin/bash

remote_info=$(git remote -v)
# echo $remote_info
remote_url=$(echo $remote_info | awk '{print $2}')
is_http_url=$(echo $remote_url | sed -n '/^http/p')
if [ ! -z $is_http_url ]
then
    echo "http remote found!!"
else
    echo "http remote not found!!"
    exit 0
fi
ssh_url=$(echo $remote_url | sed -E 's/https:\/\/github.com\/(.*)\/(.*).git/git@github.com:\1\/\2.git/')
echo $ssh_url
git remote set-url origin $ssh_url