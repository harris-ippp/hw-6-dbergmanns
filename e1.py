#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

url= 'http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General'

get= requests.get(url)
page= get.content #get the content of the website
soup= BeautifulSoup(page,'html.parser') #converting the data so it can be manipulated in python

find= soup.find_all('tr','election_item') #tr is the tag and election_item is the class. Find this element

ELECTION_ID=[]
for t in find:
    year = t.td.text
    year_id = t['id'][-5:] #get the last five numbers of the element id
    i=[year, year_id] 
    ELECTION_ID.append(i) #add to the empty list the year and the id
print(ELECTION_ID)