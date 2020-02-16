import csv
import json
import pandas as pd
import numpy as np
import re
import nltk
import time
import matplotlib.pyplot as plt
from pprint import pprint
from ast import literal_eval
from langdetect import detect_langs
from langdetect import DetectorFactory
DetectorFactory.seed=0

import urlmarker
from html import unescape

p='#|@\w*|('+ urlmarker.ANY_URL_REGEX +')'

tr_lang=['hi','gu','bn','pa','ur','ta','kn','te','ml','mr','ne']

space=' '

def fun_lang2(arg):
    r1=False
    r2=True
    prob=0
    try:
        d=detect_langs(space.join(arg['pros_text'].split()))
    except:
        return False , None,0
    for el in d:
        if el.lang in tr_lang: 
            return True,True,len(space.join(arg['pros_text'].split()))
        else:
            if el.lang=='en':
                prob=el.prob
                r1=True
            else:
                r2=False
    
        
    if r2==False and prob<0.4: 
        return False,None, 0
    else:
        return r1,False, 0
    
    ###########################################################################################################################################
    
def f_clean2(arg):
    if arg.full_text=='':
        s=unescape((arg['text']))
    else:
        s=unescape((arg['full_text']))
     
        
    s=re.sub(p,'',s) #removing mentions and urls from tweets
    s=space.join(s.split()) #compressing whitespace
    return s   
