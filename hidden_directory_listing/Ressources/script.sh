#!/bin/bash

IP_ADDRESS=$(hostname -I | awk '{print $1}')

# Takes url as argument and recursively calls itself 
# until no other link is found
curl_address() {
	curl $1 | grep "<html>"
	if [ $? -eq 1 ]; then
		curl $1 >> results.txt
	else
		URLS=`curl $1 | grep href | cut -d'"' -f 2 | tail -n +2`
		IFS=$'\n' URLS_SPLIT=($URLS)
		for str in ${URLS_SPLIT[@]}; do
			curl_address "$1$str"
		done
	fi
}

rm -rf results.txt
# Gotta put the right address in there
curl_address "http://192.168.56.101/.hidden/"
sort results.txt | uniq -u > flag.txt