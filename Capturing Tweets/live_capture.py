#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This program was used to capture tweets in real time (from 23rd May 2019 to 26th May 2019)


# In[1]:


from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
from sys import argv
import json
import csv
import pandas as pd
import numpy as np


# In[2]:


key='************************';
key_sec='******************************************';

token='******************************************';
token_sec='******************************************';


# In[3]:


name='tweets'+str(argv[1])+'.csv'

class Listener(StreamListener): 

    def on_status(self,status): 
        if not hasattr (status,'retweeted_status'): #if not a retweet
            
           s={
                    'created_at': str(status.created_at),
                    'id': str(status.id), 
                    'id_str': str(status.id_str),
                    'text' : str(status.text),
                    #'display_text_range' : str(status.display_text_range),
                    'truncated' : str(status.truncated),
                    'in_reply_to_status_id' : str(status.in_reply_to_status_id),
                    'in_reply_to_status_id_str' : str(status.in_reply_to_status_id_str),
                    'in_reply_to_user_id' : str(status.in_reply_to_user_id),
                    'in_reply_to_user_id_str' : str(status.in_reply_to_user_id_str),
                    'in_reply_to_screen_name' : str(status.in_reply_to_screen_name),
                    'place' : str(status.place),
                    'user_id' : str(status.user.id),
                    'user_id_str' : str(status.user.id_str),
                    'user_name' : str(status.user.name),
                    'user_screen_name' : str(status.user.screen_name),
                    'location' : str(status.user.location),
                    'utc_offset' : str(status.user.utc_offset),
                    'time_zone' : str(status.user.time_zone),
                    'lang' : str(status.user.lang),
                    'protected' : str(status.user.protected),
                    'verified' : str(status.user.verified),
                    'followers_count' : str(status.user.followers_count),
                    'friends_count' : str(status.user.friends_count),
                    'listed_count' : str(status.user.listed_count),
                    'favourites_count' : str(status.user.favourites_count),
                    'statuses_count' : str(status.user.statuses_count),
                    'coordinates' : str(status.coordinates)}
            
           if hasattr (status,'display_text_range'):
              s.update({'display_text_range':str(status.display_text_range)}) 
           
           if hasattr (status,'extended_tweet'):
              s.update({'extended_tweet':str(status.extended_tweet)})                 
           
           s_=json.dumps(s)
 
           with open(name,'a') as f:
               f.write(str(s_) +"\n")  


# In[4]:


auth=OAuthHandler(key,key_sec)
auth.set_access_token(token,token_sec)
l=Listener()
s=Stream(auth,l)
s.filter(track=['ElectionResults2019','Narendra','Election', 'AcceptTheVerdict','NotMyPM','ModiGoBack','Verdict2019','ModiAaRahaHai','ABPresults2019', 'Modi','Gandhi','Rahul','BJP','Congress','mahagathbandhan', 'Namo','Pappu','PM','Indian Election','Mamta','AAP','SP','BSP','TMC','trinamool congress','NDA','UPA','Bhakt','chokidar' ])

