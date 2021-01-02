#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 09:47:59 2021

@author: zackarias00
"""

import json
from difflib import get_close_matches

data = json.load(open("/your file directory to json file attached/"))

# Function that finds the word in the dictionary and returns it with the definition

def find_word():
   
    
   while True:
        definition = ''
        # Input is automatically lowercase to ensure consistency
        word = input("Enter a word: ").lower()
        choice = 'y'
        
        while True:
            # Checks for the word in the dictionary
            if word in data:
                definition = data[word]
            # Checks for a word if the first letter is capitalized
            elif word.title() in data:
                definition = data[word.title()]
            # Checks for a word where all letters are capitalized
            elif word.upper() in data:
                definition = data[word.upper()]
            # Checks for the closest match to the input word and prompts the user to affirm that this is what they meant
            elif len(get_close_matches(word, data.keys())) > 0:
                print ("Did you mean %s instead?" % get_close_matches(word, data.keys())[0])
                choice = input("Y or N? ")[0].lower()
            else:
                print("I do not think that's a word!")
                break
            
            while True:
                # Handles any errors from user input on "Did you mean?" prompt
                if choice == 'y':
                    word = get_close_matches(word, data.keys())[0]
                    definition = data[word]
                    break
                elif choice == 'n':
                    print("This is not a word! Try again!")
                    break
                elif choice != 'y' and choice != 'n':
                    print("That is not a valid choice!")
                    choice = input("Y or N? ").lower()
                else:
                    break

        
            # Outputs the definition
            if choice == 'y':
                output = definition
                for items in output:
                    print(f"{items}")
                break
            else:
                break
        break


find_word()
