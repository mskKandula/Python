import docx
import requests
from bs4 import BeautifulSoup

doc = docx.Document()

baseURL = 'https://www.tutorialspoint.com'

url = 'https://www.tutorialspoint.com/artificial_intelligence_with_python/index.htm'

while(url):

    page = requests.get(url)

    soup= BeautifulSoup(page.content,'html.parser')

    contain = soup.find('div', class_= 'mui-container-fluid')

    result = contain.find('div',class_='mui-container')

    p_tags = result.find_all('p')

    nxt_btn = result.find('div',class_='nxt-btn')

    nxt_btn_anchor = nxt_btn.find('a')

    nxt_btn_href = nxt_btn_anchor['href']

    if (nxt_btn_href.split('/')[2]=='index.htm'):
        
        break

    for p_tag in p_tags:

        doc.add_paragraph(p_tag.text)

    url = baseURL + nxt_btn_href


doc.save('python.docx')    