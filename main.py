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
# print(title)
# print(title.string)

# Commonly used types of objects
# print(type(title))  # 1. Tag
# print(type(title.string))  # 2. NavigableString
# print(type(soup))  # 3. BeautifulSoup

# 4. Comment
markup = "<p><!-- This is a comment --></p>"
soup2 = BeautifulSoup(markup, 'html5lib')
soup2_text = soup2.find("p").string
# print(soup2_text)
# print(type(soup2_text))

# Fetch title of the HTML page
title = soup.title
# print(title.text)

# Fetch all the paragraphs from the page
paras = soup.find_all("p")
# print(paras)

# Fetch all the anchor from the page
anchors = soup.find_all("a")
# print(anchors)
# Fetch all links from anchor
links = []
unique_links = set()
for link in anchors:
    links.append(link.get("href"))
    unique_links.add(link.get("href"))
# print(links)
# print(unique_links)

# Fetch first paragraph, along with details
para1 = soup.find("p")
# print(para1)

# Fetch classes in Paragraph
class1 = soup.find("p").get("class")
# print(class1)

# Fetch all the elements with class "mt-2"
class_lead = soup.find_all("p", class_="mt-2")
# print(class_lead)

# Fetch text from the tags/soup
para_text = soup.find("p").get_text()
# print(para_text)

# Fetch content
nav_bar_content = soup.find(id="navbarSupportedContent")

# .content - A tags children are available as a list
# for elem in nav_bar_content.contents:
#     print(elem)

# .children - A tags children are available as a generator
# for elem in nav_bar_content.children:
#     print(elem)

# Fetch parent
# print(nav_bar_content.parent)
# for item in nav_bar_content.parents:
#     print(item)

# print(nav_bar_content.previous_sibling)

# CSS Selector
elem = soup.select("#loginModal")
# print(elem)

# Fetch data from HTML table in dictionary format

data = '<html><table>' +\
    '<tr><td class="label"> key1 </td> <td> value1 </td></tr>' +\
    '<tr><td class="label"> key2 </td> <td> value2 </td></tr>' +\
    '<tr><td class="label"> key3 </td> <td> value3 </td></tr>' +\
    '<tr><td class="label"> key4 </td> <td> value4 </td></tr>' +\
    '</table></html>'

bs = BeautifulSoup(data, "html5lib")

# print(bs.findAll('tr'))
# print(bs.findAll('tr')[0].findAll('td')[0].string)  # first key
# print(bs.findAll('tr')[0].findAll('td')[1].string)  # first value

result = {}
for row in bs.findAll('tr'):
    aux = row.findAll('td')
    result[aux[0].string] = aux[1].string

# print(result)
