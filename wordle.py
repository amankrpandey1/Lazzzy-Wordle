#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 23:49:56 2022

@author: lazzzy
"""
import urllib
import random
import re 
import requests

iterations=0

def get_meaning(word="hello"):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+word
    response = requests.get(url)
    response = response.json()
    d={
       'meaning': response[0]['meanings'][0]['definitions'][0]['definition'],
       }
    if 'synonyms' in (response[0]['meanings'][0]['definitions'][0]).keys():
        d['synonyms'] = response[0]['meanings'][0]['definitions'][0]['synonyms']
    if 'example' in (response[0]['meanings'][0]['definitions'][0]).keys():
        d['example'] = response[0]['meanings'][0]['definitions'][0]['example']
    if 'phonetics' in (response[0]).keys():
         d['phonetics'] = response[0]['phonetics']
    return d
def random_text_generator(url=r"https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt"):
    
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
       if 'synonyms' in d.keys():
           print("synonyms: ",d['synonyms'])
       if 'example' in d.keys():
              print("example: ",d['example'])
       if 'phonetics' in d.keys():
              print("phonetics: ",d['phonetics']) 
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
            
def input_check(provided_text):
    if len(provided_text)>5 or len(provided_text)<5:
        print("word length should be equal to 5, please try again")
        return False
    elif not re.match("^[a-z]*$", provided_text):
        print("Only letters a-z allowed!, Please try again")
        return False
    else:
        return True
    
def wordle_wrapper(text_of_the_day="Hello"):
    print("**************************=============**************************")
    print("")
    print("Welcome to Lazzzy's Wordle Game!")
    print("")
    print("**************************=============**************************")
    print("")
    
    input_text = text_of_the_day.lower()
    flag = False 

    for i in range(6):
        print("Attempt "+str(i+1)+" enter your word (word length should be 5)")
        while(True):
            provided_text = input().lower()
            res = input_check(provided_text)
            if res:
                break
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
    calling_wrapper(text_of_the_day)
