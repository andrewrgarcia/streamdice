#!/bin/bash
echo "--- PYSTREAMDICE (encoder)---"

echo enter message to encode:
IFS= read -r TOKEN
echo enter key:
read -s KEY

python main/encode_main.py -m "$TOKEN" -k $KEY
