#Import Basic Librarries
import os
#!nvidia-smi

HOME = os.getcwd()
print("HOME:", HOME)
import numpy as np
import pandas as pd
import requests
from tqdm.notebook import tqdm
import copy
from bs4 import BeautifulSoup
import base64
import json

#Sample Code for 'https://www.livgolf.com/stats/fairway-hit?season=2024&tournamentId=27' Data Collections

url = "https://www.livgolf.com/stats/fairway-hit?season=2024&tournamentId=27"
r = requests.get(url) # r variable has all the HTML code
htmlContent = r.content # r returns response so if we want the code we write r.content
#print(htmlContent) # printing the code

htmlText = r.text
#print(htmlText)

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

#print(soup.prettify()) # to print html in tree structure

soup = BeautifulSoup(htmlContent, 'html.parser')


title = soup.title
#print(title)


#This line will get you all p tags of the page:
paras = soup.find_all('p')
for i in paras:
print(i)