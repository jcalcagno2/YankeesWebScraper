from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
fh = open('yanksStats.txt', 'w')

url_of_page = requests.get('https://www.baseballamerica.com/teams/1028/new-york-yankees/stats/')
soup = BeautifulSoup(url_of_page.text, 'html.parser')

table = soup.find('div', class_ = 'team-stats-category')


stats_table = pd.read_html(str(table))

print(stats_table)
fh.write(str(stats_table))

fh.close()

print("yankees will win the world series!")