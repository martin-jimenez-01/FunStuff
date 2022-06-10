#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 18:32:59 2022

@author: muertyn
"""

# Ceaser Cipher encoder and decoder
def to_hex(msg):
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
    final_msg = to_hex(coded_msg)
    
    return final_msg
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        