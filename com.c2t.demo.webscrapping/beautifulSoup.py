import requests , bs4

res = requests.get('http://localhost:8888/connect2tech.in-Selenium-Automation-Java-1.x/')
res.raise_for_status()

bSoup = bs4.BeautifulSoup(res.text)
#print(bSoup)

tds = bSoup.select('td')

for td in tds:
    print(td.getText())
   
    
  
    
   
