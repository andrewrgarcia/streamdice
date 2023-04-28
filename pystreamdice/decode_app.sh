#!/bin/bash
echo "--- PYSTREAMDICE (decoder)---"

echo enter ciphertext to decode:
IFS= read -r CIPHERTEXT
echo

echo enter key:
read -s KEY

echo token:
python main/decode_main.py -m "$CIPHERTEXT" -k $KEY