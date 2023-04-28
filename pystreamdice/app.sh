#!/bin/bash

echo --- PYSTREAMDICE : Python code for the streamdice algorithm ---
echo Andrew Garcia, 2021

echo encoder [1] or decoder [0]?
IFS= read -r boolean

if [ $boolean == '1' ]
then 
    ./encode_app.sh
else 
    ./decode_app.sh
fi 