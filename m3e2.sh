#!/bin/bash
# Bash script to solve Module 3 - Exercise 2 from C1b3rw4ll
# Decryption of files using a loop and a private key

for i in $(ls -l *.encrypted)
do 
	echo "$i"
	openssl rsautl -decrypt -in "$i" -inkey privkey.pem >> all_decrypted.xml
done
