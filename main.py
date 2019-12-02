import requests
from bs4 import BeautifulSoup


url = 'http://www.cvm.gov.br/menu/afastamentos/termos_compromisso.html'

session = requests.Session()
r = session.get(url=url)

soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find('table', {'class': 'resultsarchive-table'})
print(table)