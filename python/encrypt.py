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


args = vars(ap.parse_args())

# print('double-check:')
# print(decrypt(encrypt(args["message"], args["key"]), args["key"]))

# print('\nencrypted message:')
print(encrypt(args["message"], args["key"]))
