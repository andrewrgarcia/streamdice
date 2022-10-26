#!/bin/bash

echo --- STREAMDICE CIPHER ---
echo Andrew Garcia, 2021

echo encrypt [1] or decipher [0]?
IFS= read -r boolean

if [ $boolean == '1' ]
then 
    echo enter message to encrypt:
    IFS= read -r TOKEN
    echo enter key:
    read -s KEY

    echo --- message encrypted! ---
    python encrypt.py -m "$TOKEN" -k $KEY
else 
    echo enter ciphertext to decipher:
    IFS= read -r CIPHERTEXT
    echo

    echo enter key:
    read -s KEY

    echo token:
    python decipher.py -m "$CIPHERTEXT" -k $KEY
fi 