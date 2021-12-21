import requests
from bs4 import BeautifulSoup


url = 'https://www.tutorialspoint.com/artificial_intelligence_with_python/artificial_intelligence_with_python_supervised_learning_classification.htm'

page = requests.get(url)

soup= BeautifulSoup(page.content,'html.parser')

contain = soup.find('div', class_= 'mui-container-fluid')

result = contain.find('div',class_='mui-container')

p_tags = result.find_all(['p','pre','h2','h3','li'])

# print(p_tags)

for p_tag in p_tags:
    if (p_tag.name == 'h2' or p_tag.name =='h3'):
        print(p_tag)
