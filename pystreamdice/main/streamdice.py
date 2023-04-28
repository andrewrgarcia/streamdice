'''
streamdice.py
Andrew Garcia, 2021
https://github.com/andrewrgarcia/streamdice

Oldest implementation of streamdice algorithm. Written in Python
* Encrypts all characters, including spaces. 
* Requires 1 key as an input, but  the ROOT block and SEQUENCE blocks of the 
streamdice algorithm are preserved. 
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 13:15:08 2021

@author: andrew
"""
import string
import numpy as np
import random

    
def encrypt(msg, key):
    
    root, *sequence = list(key)
    sequence = np.array(sequence).astype('int')
    N_w = len(key)-1

    np.random.seed(int(root))        
    zeta1 = np.random.random(N_w)+np.random.randint(1,40,N_w)
        
    seeds =  (sequence+zeta1)**2
    # print('seeds',seeds.astype('int'))
        
    extraspace = (N_w - len(msg)%N_w) if len(msg)%N_w!=0 else 0
    
    msg = msg + extraspace*' '
    
    splits = np.array_split(list(msg), N_w)
    
    # print(splits)
    keys = list(string.printable)[:-5]
    'remove potential escape characters'
    keys.remove('\\')
    keys.remove('`')
    keys.remove('\'')

    # print(keys)
    
    numkeys = len(keys)
    key_positions = np.arange(numkeys)
        
    warped_msg = []
    for seed, frag in zip(seeds,splits):
        np.random.seed(int(seed))
        key_positions = np.arange(numkeys)
        
        warpedfrag = []
        for i in frag:
            
            np.random.shuffle(key_positions)
            keyidx = keys.index(i)
            idx = np.argwhere(key_positions==keyidx)[0][0]
            warped_key = keys[idx]

            warpedfrag.append(warped_key)
        
        warpedfrag = ''.join(warpedfrag)
        
        # print(frag)
        # print(warpedfrag)
        warped_msg.append(warpedfrag)
    
    warped_msg = ''.join(warped_msg)
    
    return warped_msg


def decrypt(msg,key):
    
    root, *sequence = list(key)
    sequence = np.array(sequence).astype('int')
    N_w = len(key)-1
    np.random.seed(int(root))        
    zeta1 = np.random.random(N_w)+np.random.randint(1,40,N_w)
    
    seeds =  (sequence+zeta1)**2
    
    splits = np.array_split(list(msg), N_w)
    
    keys = list(string.printable)[:-5]
    'remove potential escape characters'
    keys.remove('\\')
    keys.remove('`')
    keys.remove('\'')
    
    numkeys = len(keys)
    key_positions = np.arange(numkeys)

    ordered = []
    for seed, frag in zip(seeds,splits):
        
        np.random.seed(int(seed))
        
        # print(frag)
        ordfrag = []
        oldkeyposits = key_positions.copy()
        for i in frag:
            
            np.random.shuffle(key_positions)
            keyidx = keys.index(i)
            locs = [list(key_positions).index(k) for k in oldkeyposits]
            
            realidx = locs.index(keyidx)
            idx = np.argwhere(np.arange(numkeys)==realidx)[0][0]
            key = keys[idx]
            ordfrag.append(key)
            
            # keyposits_order = [key_positions[j] for j in locs]
            # print('\n',locs)
            
        ordfrag = ''.join(ordfrag)
        # print(ordfrag)
        ordered.append(ordfrag)
        
    ordered = ''.join(ordered)
    
    return ordered
    

# key = '123456'
# msg = '&&** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua (Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat).**&& != #43435563'
# msg= "Hello World! :) @andrew"

# print(encrypt(args["message"], args["key"]))
# print(decrypt(encrypt(args["message"], args["key"]), args["key"]))
# print(decrypt(args["message"], args["key"]))
