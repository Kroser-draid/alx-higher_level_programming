#!/bin/bash
#this script should print the size of the body
curl -w "%{size_download}\n" -o /dev/null -s "$1"
