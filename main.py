import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/"


# Step 1: Get the HTML
r = requests.get(url)
html_content = r.content
# print(html_content)

# Step 2: Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify())


# Step 3: HTML Tree traversal
title = soup.title
print(title)
print(title.string)
