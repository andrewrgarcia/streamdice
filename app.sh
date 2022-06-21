#!/bin/bash

ENCRYPT=$1


echo -------- STREAMDICE --------
echo A stream cipher written in C++
echo Andrew Garcia, 2022
echo

encryptit(){

echo enter message to encrypt:

IFS= read -r MSG

echo enter key:
read -s KEY

echo --- message encrypted! ---
./streamdice.k $MSG $KEY $ENCRYPT

}

encryptit()



# process(){
	 
# 	echo enter secret message to decipher:

# 	IFS= read -r MSG

# 	echo enter key:
# 	read -s KEY

#     echo --- message decrypted! ---
# ./streamdice.k $MSG $KEY $ENCRYPT
# }