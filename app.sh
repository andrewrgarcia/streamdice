#!/bin/bash

ENCRYPT=$1


encryptit(){

	# echo enter message to encrypt:
	# IFS= read -r MSG
	# echo $MSG
	echo enter key:
	read -s KEY
	# echo --- message encrypted! ---
	./streamdice.k $KEY $ENCRYPT

}

decipher(){

	# echo enter secret message to decipher:
	# IFS= read -r MSG
	echo enter key:
	read -s KEY
    # echo --- message deciphered! ---
	./streamdice.k  $KEY $ENCRYPT

}

if [ $ENCRYPT == '-h' ]
then 
	echo About:
	echo -------- STREAMDICE --------
	echo A stream cipher written in C++
	echo Andrew Garcia, 2022
	echo
	echo "Disclaimer: Use At Your Own Risk"
	echo This program is free software. It comes without any warranty, to
	echo the extent permitted by applicable law. You can redistribute it
	echo and/or modify it under the terms of the MIT LICENSE, as published by Andrew Garcia. See
	echo https://github.com/streamdice for more details.
	echo 
	echo About Keys:
	echo Your key is an N-digits integer which is used to encrypt and decrypt the input information 
	echo The number of digits cannot be larger than the character length of the information to be encrypted
	echo
	echo Usage:
	echo "enter the name of the app followed by either 1 to encrypt or 0 to decipher. i.e."
	echo "./StreamDice 1 	# encryption "
	echo "./StreamDice 0 	# deciphering"
	echo
	echo "(Characters not supported: \, ?, |)"


elif [ $ENCRYPT == 0 ]
then 

	decipher

else
	encryptit
fi

