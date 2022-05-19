#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 23:49:56 2022

@author: lazzzy
"""
import urllib
import random
import regex as re
import requests

iterations=0

def get_meaning(word="hello"):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+word
    response = requests.get(url)
    response = response.json()
    d={
       'meaning': response[0]['meanings'][0]['definitions'][0]['definition'],
       }
    return d
def random_text_generator(url="https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt"):
    
    file = urllib.request.urlopen(url)
    word_list=[]
    for line in file:
    	decoded_line = line.decode("utf-8")
    	word_list.append(decoded_line)
    return random.choice(word_list)


def wordle(provided_text="",input_text=""):
   global iterations
   if iterations==0:
       iterations+=1
   if provided_text==input_text:
       print("Congratulations correct guess in ",iterations," attempt(s)\n")
       d = get_meaning(provided_text)
       print("word: ",provided_text)
       print("meaning: ",d['meaning'])
       return True
   else:
       iterations+=1
       for i in range(0,len(provided_text)):
           if provided_text[i] in input_text:
               index = input_text.index(provided_text[i])
               if index==i:
                   print(provided_text[i], " is at correct position",i+1)
                   print("")
               else:
                   print(provided_text[i]," is present but at random position")
                   print("")
       return False
            

def wordle_wrapper(text_of_the_day="Hello"):
    print("**************************=============**************************")
    print("")
    print("Welcome to Lazzzy's Wordle Game!")
    print("")
    print("**************************=============**************************")
    print("")
    
    input_text = text_of_the_day.upper()
    flag = False 

    for i in range(6):
        print("Attempt "+str(i+1)+" enter your word (word length should be 5)")
        provided_text = input().upper()
        if len(provided_text)>5:
            print("word length should be equal to 5, please try again")
            provided_text = input().upper()
        print("")
        if  wordle(provided_text,input_text):
            flag = True
            return flag
    
    if not flag:
        print("Failed! Max Attempts reached, Please try again!") 

def calling_wrapper(text_of_the_day="Hello"):
    while(True):
        flag = wordle_wrapper(text_of_the_day)
        if flag:
            break
        res = input("\nWould you like to play again? (y/n): ")
        if(res!='y'):
            break

if __name__=="__main__":
    
    url="https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt"
    text_of_the_day = random_text_generator(url)
    calling_wrapper('crept')