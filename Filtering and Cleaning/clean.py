import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import random
import pickle
import unicodedata
import emoji
from sys import argv
from time import time,sleep
from nltk.corpus import stopwords
from nltk import RegexpTokenizer



#language based stopwords
s_w2=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 
     'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 
     'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
     'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 
     'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and',
     'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'between', 'into', 'through', 
     'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'under', 
     'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each',
      'other', 'some', 'such', 'only', 'same', 'so', 'than', 'too', 'very', 's', 't', 
     'can', 'will', 'just', 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y','could','would']


    
#context based stopwords
swmod3=['rahul','modi','bjp','congress','mamta','mamata','rg','gandi','atishi','sachin',
    'pragya','gandhi','aap','kejriwal','rahulgandhi','navjot', 'singh' ,'sidhu','siddhu'
    ,'sonia','singh','captain','cap','soniagandhi','vadra','smriti', 'irani','swami',
    'kerala','kerla','tn','tamilnadu','tamil','nadu','rajdeep','gandhis','pm','president','kamal','kamalnath','swara'
     ,'kunal','kanhaiya', 'kumar','bhaskar','kamra','amit','shah','bjd','shiv','shivsena','rjd','bsp','sp','tmc'
    ,'yogi','adityanath','mns','src','sir','madam','sh','shree','smt','shreemati','ji','banerjee','chandrababu', 'naidu'
    , 'rss','pgv','hindu','hindus','muslim','muslims','christian','christians','chowkidar','cong']  

for e in s_w2:
    swmod3.append(e)

import urlmarker
from html import unescape

p=r'#|@\w*|\d*|<.*?>|('+ urlmarker.ANY_URL_REGEX +')'
ep=u'[\U0001F602-\U0001F64F]'
emoji_pattern = re.compile("["
u"\U0001F600-\U0001F64F"  # emoticons
u"\U0001F300-\U0001F5FF"  # symbols & pictographs
u"\U0001F680-\U0001F6FF"  # transport & map symbols
u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
u"\U00002702-\U000027B0"
u"\U000024C2-\U0001F251"
"]+", flags=re.UNICODE)



def f_all(arg): #This is used to perform text cleaning on tweet's text
    s=''
    if arg['full_text']!='':
        s=arg['full_text']
    else:
        s=arg['text']
    #############################################################################################################    
    #remove emoji
    space=' '
    s_=space.join(char for char in s )#break string into characters seperated by spaces(this is needed to seperate 
    #adjacently joined emojis (other wise they are not recongnised by unicodedata.name() ))

    #print(s_)
    l=emoji_pattern.findall(s_)
    underscore='x'
    #print(l)
    for e in l:#subsitute using emojis identified by emoji_pattern
        try:
            s=re.sub(e,' '+str(underscore.join((unicodedata.name(e).split()))) +' ',s)
            #s=re.sub(e,' ',s)
        except:
            pass

    for char in s : #subsitute using emojis identified by emoji library 
        if char in emoji.UNICODE_EMOJI:
            x=emoji.demojize(char).strip(':').replace('_','x')
            s=re.sub(char,' '+str(x) +' ',s)
            #s=re.sub(char,' ',s)
    
    #############################################################################################################
    #basic cleaning
    space=' '
    s=s.lower() 
    s=unescape((s))    
    s=re.sub(p,'',s)    
    s=space.join(s.split())
    
    #############################################################################################################
    #remove non-alphanumeric
    
    s=re.sub('[^a-zA-Z ]+',' ',s) 
    
    #############################################################################################################
    #remove stopwords
    s_=''
    l=s.split()
    #print(l)
    for e in l:
        if e not in swmod3:
            s_=s_+' '+e
    
    return s_


def f_all_loc(arg): #This is used to perform text cleaning on "location" and "det_location" fields of tweet
    s=''
    if arg['']!='':
        s=arg['det_location']
    else:
        s=arg['location']
    #############################################################################################################    
    #remove emoji
    space=' '
    s_=space.join(char for char in s )#break string into characters seperated by spaces(this is needed to seperate 
    #adjacently joined emojis (other wise they are not recongnised by unicodedata.name() ))

    #print(s_)
    l=emoji_pattern.findall(s_)
    underscore='x'
    #print(l)
    for e in l:#subsitute using emojis identified by emoji_pattern
        try:
            s=re.sub(e,' '+str(underscore.join((unicodedata.name(e).split()))) +' ',s)
            #s=re.sub(e,' ',s)
        except:
            pass

    for char in s : #subsitute using emojis identified by emoji library 
        if char in emoji.UNICODE_EMOJI:
            x=emoji.demojize(char).strip(':').replace('_','x')
            s=re.sub(char,' '+str(x) +' ',s)
            #s=re.sub(char,' ',s)
    
    #############################################################################################################
    #basic cleaning
    space=' '
    s=s.lower() 
    s=unescape((s))    
    s=re.sub(p,'',s)    
    s=space.join(s.split())
    
    #############################################################################################################
    #remove non-alphanumeric
    
    s=re.sub('[^a-zA-Z ]+',' ',s) 
    
    return s


