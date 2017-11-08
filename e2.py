from bs4 import BeautifulSoup
import requests

url = 'http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General'
get = requests.get(url)
page= get.content 
soup = BeautifulSoup(page,'html.parser') 
find= soup.find_all('tr','election_item')

ELECTION_ID=[]
for t in find:
    year = t.td.text
    year_id = t['id'][-5:]
    i=[year,year_id]
    ELECTION_ID.append(i)
    
Year = [item[0] for item in ELECTION_ID]
ID = [item[1] for item in ELECTION_ID]
dictionary = dict(zip(ID, Year))
dictionary

for t in ID:
    base = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'
    replace_url = base.format(t)
    response = requests.get(replace_url).text
    Year_data = "president_general_"+ dictionary[t] +".csv"
    with open(Year_data, 'w') as output:
        output.write(response)