#!/usr/bin/bash
#this script should print the size of the body
var="$1"
curl -w "%{size_download}\n" -o /dev/null -s "$var"
