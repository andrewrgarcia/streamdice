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

    
print(decrypt(args["message"], args["key"]))
# tests
# print(decrypt("?h+9llhr3ZK,#<aF$91y2)IR3l8|t%?| f?Dcv)Q!2Aij^4,8wnvZ02hwU8Ax?N0Qga=^b<Kc'V#9)UO9Bt\ij(gFe", args["key"]))
# print(decrypt('Rrs"IY6(na/-z|H}.)y}Kb{RToDcwpPx;nai1:uuvLAy"3|sRMpk{w4z<{y;MtzDPdQ"Zb%AsI2_a46v3vtV'+"'<(gFe", args["key"]))

