#!/bin/bash

for i in $(ls -l *.encrypted)
do 
	echo "$i"
	openssl rsautl -decrypt -in "$i" -inkey privkey.pem >> all_decrypted.xml
done
