import requests
from bs4 import BeautifulSoup

url = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'

page = requests.get(url)

# print(page)

# print(page.content)

soup= BeautifulSoup(page.content,'html.parser')

result = soup.find(id = 'ResultsContainer')

# print(result)

# find_all gives us an iterator
job_elems= result.find_all('section', class_= 'card-content')

for job_elem in job_elems:

    # print(job_elem)

    title_elem = job_elem.find('h2', class_='title')

    company_elem = job_elem.find('div', class_='company')

    location_elem = job_elem.find('div', class_='location')

    # if there are any breaks or adds in between 
    if None in (title_elem, company_elem, location_elem):
        continue

     # strip to remove any whitespaces
    print(title_elem.text.strip())

    print(company_elem.text.strip())

    print(location_elem.text.strip())

    print()