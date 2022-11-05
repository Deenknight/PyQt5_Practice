#Use Shift+Alt+A to quickly comment-out and uncomment code

from bs4 import BeautifulSoup

import requests
import shutil

html_text = requests.get("https://en.wikipedia.org/wiki/University_of_Alberta")
soup = BeautifulSoup(html_text.text, 'lxml')

""" 
# Find the title of the article and print it out
header = soup.find('h1', id='firstHeading')
print(header.text)
"""

""" 
# Find all urls, and only print out the ones that link to a seperate web link
urls = soup.findAll('a', href=True)

[print(a['href']) for a in urls if a['href'].startswith('http')] 
"""

"""
# Find the first image on the page, and print out its source url
images = soup.findAll('img')    
firstImage = images[0]
imgURL = firstImage.attrs['src']
print(imgURL)
"""

""" 
# Find image
images = soup.findAll('img')
firstImage = images[2]
imgURL = firstImage.attrs['src']
urlBase = "https:"

# Make a request for the specific image
r = requests.get(urlBase + imgURL, stream=True)

if r.status_code == 200: # status_code == 200 if successful
    with open("imgs\\img.png", 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
 """



