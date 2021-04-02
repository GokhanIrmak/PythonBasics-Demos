import requests
from bs4 import BeautifulSoup
r=requests.get("http://python.beispiel.programmierenlernen.io/index.php")

# print(r.status_code)
# print(r.headers)
# print(r.text)

doc = BeautifulSoup(r.text,"html.parser")

for p in doc.find_all("p"):
    print(p.text)
    print(p.attrs) #Print attributes of 'p'


