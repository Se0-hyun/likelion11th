from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.subway.co.kr/?mobile')
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')
name = soup.find_all('strong', 'title')
tab = soup.find_all('div', 'tab')


print("\n클래식")
for i in range(5):
    print("- " + name[i].get_text())

print("-----------------------------------\n프레쉬&라이트")
for i in range(5, 10):
    print("- " + name[i].get_text())

print("-----------------------------------\n프리미엄")
for i in range(10, 16):
    print("- " + name[i].get_text())

print("-----------------------------------\n아침메뉴")
for i in range(16, 18):
    print("- " + name[i].get_text())
