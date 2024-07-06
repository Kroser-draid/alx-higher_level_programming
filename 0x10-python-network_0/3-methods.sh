#!/bin/bash
#script that shows body of response
curl -sX OPTIONS -i "$1" | grep "Allow" | awk -F ': ' '{print $2}'
