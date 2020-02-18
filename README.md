# Sentiment Analysis on Loksabha Elections 2019 
This was my Summer Internship Project at DRDO (Defense Research and Development Organization), New Delhi under the mentorship of Mr Amit Dhawan (Scientist-F) 

## Overview
Tweets related to Indian Assembly election 2019 result were captured. These tweets were then filtered by location and language and then they were cleaned. Bigram tokens were obtained from the tweets. Word2Vec model was then trained using the obtained corpus of tweets. 
Around 5,003 tweets were randomly picked and manually labelled into 3 classes of sentiments (positive, neutral and negative). Using the trained word2vec model, tokens of labelled data were embedded. Then labelled data was partitioned into train-test split (70 to 30 ratio). Training data-set was then used to train a linear SVM (Support Vector Machine) model. This model was then used to assess the sentiments from remaining unlabeled tweets. Sentiments were presented in form of Bigram v/s Frequency curves and color shaded Maps (as per sentiment intensity).


## Technologies Used: 
    -Support Vector Machine (ML classifier used to identify tweets as having positive, neutral and negative sentiment) 
    -Word2Vec (a Neural Network based model used for embedding tokens ) 
    -langdetect (a pretrained ML model; to detect language of tweet) 
    -Vader ( a lexical text analyzer; to compare accuracy of trained SVM against Vader’s accuracy) 
    -Google Cloud Platform (entire project was originally built on a GCP Instance)

## Libraries Used: 
sklearn, genism, nltk, numpy, pandas, matplotlib, geopandas, tweepy, lanngdetect, geopy (Nominatim API) , re, unicodedata, emoji, urlmarker, json, ast, pickle, sys, time, os

## Data Used: 
    -Lok Sabha election Tweets were collected via twitter api from 23rd May 2019 to 26th May 2019. After cleaning and filtering, it          turned out to be a collection of 5,27,474 tweets in English language along with fields like tweet id, user name & id, creation           time, location, followers count, favorite count, verified status etc. 
    -5,303 random tweets from above data were manually labelled into positive, neutral and negative classes to form training and test        set (70-30 split) 
    -“GeoLite2-City” Database was used to obtain names of 2,034 Indian Cities (which were used to identify Indian tweets in case a user       didn’t mention country name or state name in their account location but instead just mentioned city name)
    -“Indian Census 2011” based shapefile was used to plot a district-wise Indian map
