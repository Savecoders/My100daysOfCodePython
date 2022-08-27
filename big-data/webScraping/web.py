from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/The_Avengers-848228'

# result from request
result = requests.get(website)

content = result.text

# extract data from page
soup = BeautifulSoup(content, 'lxml')

# deplot html code in print
# print(soup.prettify())

# return the html element exam: article
# class_ = class of html <article class='main-article'>

box = soup.find('article', class_='main-article')

title = box.find('h1').get_text()

plot = box.find('p', class_='plot').get_text(strip=True, separator='')

# delete spaces using strip
transcript = box.find(
    'div', class_='full-script').get_text(strip=True, separator='\n')

# w is writting mode
with open(f'{title}.txt', 'w') as file:
    file.write(plot)
    file.write(transcript)
