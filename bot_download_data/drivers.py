import requests
from bs4 import BeautifulSoup

session = requests.Session()
r = session.get(url='https://www.formula1.com/en/results.html/2014/drivers.html')

soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find('table', {'class': 'resultsarchive-table'})
