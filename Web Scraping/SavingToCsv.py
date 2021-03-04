from bs4 import BeautifulSoup
import requests 
import pandas as pd

egr_jobs = {}

url = "https://boston.craigslist.org/search/egr"

response = requests.get(url)

# print(response)

# print(response.content)

soup = BeautifulSoup(response.content,'html.parser')

# print(soup)

result = soup.find("ul",class_="rows")

# print(rows)

rows = result.find_all(class_='result-info')

for idx,row in enumerate(rows):
    # print(row)
    title_tag = row.find('a')

    title = title_tag.text if title_tag else 'N/A'

    link_tag = row.find('a')

    link= link_tag.get('href') if link_tag else 'N/A'

    # descriptionResponse = requests.get(link)

    # descriptionSoup = BeautifulSoup(descriptionResponse.content,'html.parser')

    # description_tag = descriptionSoup.find('section',id ='postingbody')

    # description = description_tag.text if description_tag else 'N/A'

    place_tag = row.find('span',class_='result-hood')

    place = place_tag.text.strip()[1:-1] if place_tag else 'N/A'

    time_tag = row.find('time',class_="result-date")

    time = time_tag.get("datetime").split(" ")[0] if time_tag else 'N/A' 

    # print(time)

    egr_jobs[idx] = [title,place,time,link]
   

egr_jobs_df = pd.DataFrame.from_dict(egr_jobs, orient = 'index', columns = ['Job Title','Location','Date', 'Link'])


# egr_jobs_df.head()


egr_jobs_df.to_csv('egr_jobs.csv')







