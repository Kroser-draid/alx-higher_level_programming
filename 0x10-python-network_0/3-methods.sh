#!/bin/bash
#script that shows body of response
curl -s -X OPTIONS -i "$1" | awk -F': ' '/^Allow/{print $2}'
