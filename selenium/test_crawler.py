import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()

#html = urllib3.urlopen(self,'get',"http://yahoo.com")
http = urllib3.PoolManager()
req = http.request('GET', 'https://yahoo.com')
print(req.status)
html = req.data
soup = BeautifulSoup(html, "html.parser")
print(soup.find_all('a'))
#print(soup.a)
