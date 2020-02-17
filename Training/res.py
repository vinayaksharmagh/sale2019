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
from scipy import sparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.utils import shuffle
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score, ShuffleSplit
from sklearn.multiclass import OneVsRestClassifier
from sklearn.multiclass import OneVsOneClassifier
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
from nltk import RegexpTokenizer
from sklearn.decomposition import PCA, TruncatedSVD
import matplotlib
import matplotlib.patches as mpatches
import itertools


###########################################################################################################################################


def plot_LSA(test_data, test_labels, savepath="PCA_demo.csv", plot=True):
        lsa = TruncatedSVD(n_components=2)
        lsa.fit(test_data)
        lsa_scores = lsa.transform(test_data)
        color_mapper = {label:idx for idx,label in enumerate(set(test_labels))}
        color_column = [color_mapper[label] for label in test_labels]
        colors = ['green','blue','red']
        if plot:
            plt.scatter(lsa_scores[:,0], lsa_scores[:,1], s=8, alpha=.8, c=test_labels, cmap=matplotlib.colors.ListedColormap(colors))
            red_patch = mpatches.Patch(color='red', label='neg')
            green_patch = mpatches.Patch(color='green', label='pos')
            blue_patch = mpatches.Patch(color='blue', label='neu')
            plt.legend(handles=[red_patch, green_patch,blue_patch], prop={'size': 30})
            
            
###########################################################################################################################################

def get_average_word2vec(tokens_list, vector, k=300):
    #this function obtains a 300 feature vector corrosponding to each tweet by averaging word2vec features of 
    #each token in the tweet
    
    if len(tokens_list)<1:
        return np.zeros(k)

    
    vectorized = [vector[word] if word in vector else np.zeros(k) for word in tokens_list] 
    #Here vectorrized is a 2d list, at ith row it contains all theta values(or word2vec score) for word i
    #in sentence(/token_list) 
        
    length = len(vectorized)
    summed = np.sum(vectorized, axis=0)
    averaged = np.divide(summed, length)
    return averaged

def get_word2vec_embeddings(w2v, df):
    embeddings = df['tokens'].apply(lambda x: get_average_word2vec(x, w2v))
    return list(embeddings)

###########################################################################################################################################

def plot_confusion_mat(cm,target_names,title='Confusion matrix',cmap=None,normalize=True):
#code by George Fisher (source https://www.kaggle.com/grfiv4/plot-a-confusion-matrix)

    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]


    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    #for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
    for i in range (cm.shape[0]):
        for j in range (cm.shape[1]):
            if normalize:
                plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                         horizontalalignment="center",
                         color="white" if cm[i, j] > thresh else "black")
            else:
                plt.text(j, i, "{:,}".format(cm[i, j]),
                         horizontalalignment="center",
                         color="white" if cm[i, j] > thresh else "black")


    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    plt.show()
