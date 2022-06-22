#!/bin/bash

ENCRYPT=$1


encryptit(){

	# echo enter message to encrypt:
	# IFS= read -r MSG
	# echo $MSG
	echo enter key \#1:
	read -s KEY
	echo enter key \#2:
	read -s KEY2
	# echo --- message encrypted! ---
	build/streamdice $KEY $KEY2 $ENCRYPT

}

decipher(){

	# echo enter secret message to decipher:
	# IFS= read -r MSG
	echo enter key \#1:
	read -s KEY
	echo enter key \#2:
	read -s KEY2
    	# echo --- message deciphered! ---
	build/streamdice $KEY $KEY2 $ENCRYPT

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
	echo the extent permitted by applicable law. 
	echo
	echo Inputs:
	echo "[ encrypt ] type int;    range:   1 or 0 (True or False)"
	echo [ key \#1 ]    type long;   range:   0 to 2147483647  // keep it shorter than 10 digits
	echo "[ key \#2 ]    type long;   range:   1 to (2147483647 or < message_size)"
	echo
	echo Characters not supported:
	echo " \  ? | \" "
	echo
	echo Input command format for app.sh executable:
	echo ./streamdice [ encrypt[1]/decrypt[0] ]  %
	echo
	echo Usage:
	echo "enter the name of the app followed by either 1 to encrypt or 0 to decipher. i.e."
	echo "./StreamDice 1 	# encryption "
	echo "./StreamDice 0 	# deciphering"
	echo



elif [ $ENCRYPT == 0 ]
then 

	decipher

else
	encryptit
fi

