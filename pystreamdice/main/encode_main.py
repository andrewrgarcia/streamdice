#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 13:15:08 2021

@author: andrew
"""

from streamdice import encrypt, decrypt

import argparse


ap = argparse.ArgumentParser()

ap.add_argument("-k", "--key", default = '12345',
                type = str, help="encryption key")

ap.add_argument("-m", "--message", default = 'Hello', type = str, help="message to encrypt/decrypt")


# args = vars(ap.parse_args())
args = ap.parse_args()

original = args.message
encoded = encrypt(original, args.key)
decoded = decrypt(encoded, args.key)[:len(original)]

print(f'--- message encoded! ---\n{encoded}' if original == decoded else 'Sorry: stream-cipher does not pass decoding check! Try another message OR add a random character to your message i.e. ! # and try again') 
