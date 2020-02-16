#!/usr/bin/env python
# coding: utf-8

# In[1]:


#There were some breaks during live capture of tweets (due to some twitter api exceptions).Thus, following code was used to 
#recover tweets that were lost due to such breaks.


# In[2]:


from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
from tweepy import error
from time import sleep
import json
import csv
from sys import argv
import pandas as pd
import numpy as np

def swap(x,y):
    return y,x


# In[3]:


#In twitter api, there are more limits on capturing past tweets than on capturing live tweets.Therefore, two different
#pairs of token and key were used in alternate manner in case of an exception

key1='************************';
key_sec1='******************************************';

token1='******************************************';
token_sec1='******************************************';

key2='************************';
key_sec2='******************************************';

token2='******************************************';
token_sec2='******************************************';


# In[ ]:


query='ElectionResults2019%20OR%20Narendra%20OR%20Election%20OR%20AcceptTheVerdict%20OR%20NotMyPM%20OR%20ModiGoBack%20OR%20Verdict2019%20OR%20ModiAaRahaHai%20OR%20ABPresults2019%20OR%20Modi%20OR%20Gandhi%20OR%20Rahul%20OR%20BJP%20OR%20Congress%20OR%20mahagathbandhan%20OR%20Namo%20OR%20Pappu%20OR%20PM%20OR%20Mamta%20OR%20AAP%20OR%20SP%20OR%20BSP%20OR%20TMC%20OR%20NDA%20OR%20UPA%20OR%20Bhakt%20OR%20chokidar%20OR%20trinamool'+ ' -filter:retweets'


# In[ ]:


name='tweets2'+str(argv[1])+'.csv'

#Here, we are capturing tweets that arrived after a tweet with id==oldest_id and before a tweet with id==latest_id 
oldest_id='******************'
latest_id='******************'
t=latest_id
count =1

bl=True
    
while bl:
       
        try:
            auth=OAuthHandler(key,key_sec)
            auth.set_access_token(token,token_sec)
            api=API(auth) 

            i=0
            for tweet in Cursor(api.search,q=query,since_id=oldest_id , max_id=latest_id,tweet_mode='extended').items(): 
                #Note that this loop goes from latest to oldest and not the other way around
                s={
                    'created_at': str(tweet.created_at),
                    'id': str(tweet.id), 
                    'id_str': str(tweet.id_str),
                    'text' : str(tweet.full_text),
                    'truncated' : str(tweet.truncated),
                    'in_reply_to_status_id' : str(tweet.in_reply_to_status_id),
                    'in_reply_to_status_id_str' : str(tweet.in_reply_to_status_id_str),
                    'in_reply_to_user_id' : str(tweet.in_reply_to_user_id),
                    'in_reply_to_user_id_str' : str(tweet.in_reply_to_user_id_str),
                    'in_reply_to_screen_name' : str(tweet.in_reply_to_screen_name),
                    'place' : str(status.place),
                    'user_id' : str(tweet.user.id),
                    'user_id_str' : str(tweet.user.id_str),
                    'user_name' : str(tweet.user.name),
                    'user_screen_name' : str(tweet.user.screen_name),
                    'location' : str(tweet.user.location),
                    'utc_offset' : str(tweet.user.utc_offset),
                    'time_zone' : str(tweet.user.time_zone),
                    'lang' : str(tweet.user.lang),
                    'protected' : str(tweet.user.protected),
                    'verified' : str(tweet.user.verified),
                    'followers_count' : str(tweet.user.followers_count),
                    'friends_count' : str(tweet.user.friends_count),
                    'listed_count' : str(tweet.user.listed_count),
                    'favourites_count' : str(tweet.user.favourites_count),
                    'statuses_count' : str(tweet.user.statuses_count),
                    'coordinates' : str(tweet.coordinates)
                    }
            
        
                if hasattr (tweet,'display_text_range'):
                  s.update({'display_text_range':str(tweet.display_text_range)}) 
               
                s_=json.dumps(s)
                with open(name,'a') as f:
                   f.write(str(s_) +"\n") 
                
                i=i+1
                t=str(tweet.id)
                #print(t+'  ',i)            
                if i%50==0: #after every 50th tweet, pause for 5s so as to keep rate within api limits
                    sleep(5)
                
            bl=False
    
    
    
        except error.TweepError:
            print('retrying '+ t)   
            if end_id!=t: 
                count=1
    
            token,token2=swap(token,token2) #swap credentials in order to try with one whose api limit isn't exceeded.
            token_sec,token_sec2=swap(token_sec,token_sec2)
            latest_id=t 
            sleep(2*count) #increase pause time exponentially with increase in number of exceptions
            count=count+1 
            pass

