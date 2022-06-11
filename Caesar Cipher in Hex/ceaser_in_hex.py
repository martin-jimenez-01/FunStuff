#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 18:32:59 2022

@author: muertyn
"""
from numpy import nan as NAN

# Ceaser Cipher encoder and decoder
def english_to_hex(msg):
    hex_msg = ''
    for i in range(len(msg)):
        hex_msg += format(ord(msg[i]), 'x')
        
    return hex_msg

def encoder(msg, key):
    # type checking
    if not isinstance(msg, str):
        print("msg must be a string")
        return
    
    if not isinstance(key, int):
        print("key must be an int")
        return

    #transform to 
    coded_msg =''
    for i in range(len(msg)):   
        if msg[i] == ' ':
            continue
        coded_msg += chr(ord(msg[i]) + key)
    
    # convert to hex
    final_msg = english_to_hex(coded_msg)
    
    return final_msg

def solver(original_msg, key = NAN):#input no spaces
    if key == NAN:
        return "Error: need a key top solve"
    
    if len(original_msg) % 2 != 0:
        return "Error: the original message character count is not an even number. It should be."
    
    # convert the hex into decimal
    deciphered = ''
    pair = ''
    i = 0
    while(i != len(original_msg)):
        # grab the hex pair 
        pair = original_msg[i] + original_msg[i+1] 
        # turn hex into decimal
        decimal = int(pair, 16)
        # apply the key backwards
        decimal -= key
        # turn into english add to the decoded, final msg
        deciphered += chr(decimal)
        # increment i by 2 
        i += 2 
        
    return deciphered 
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
