from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.baskinrobbins.co.kr/menu/list.php?top=A')
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')
name = soup.find_all('span', 'ice_name')

i = 0
for i in range(len(name)):
    i += 1
    print(i, "위: ", name[i-1].get_text())
