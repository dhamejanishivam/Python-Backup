import requests
from bs4 import BeautifulSoup
import html5lib
from selenium import webdriver


url = "https://www.codewithharry.com/"

 # Step 1 - Get the HTML

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

 # Step 2 - Parse the HTML
 
soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)

 # Step 3 - HTML tree traversal

"""
Commanly used type of objects - 
title = soup.title
print(type(title))        #  1. Tag
print(type(title.string)) #  2. NavigableString
print(type(soup))         #  3. Beautiful Soup
                          #  4. Comment
"""

# Get the title of html page 
title = soup.title


# Get all the paragraph from the page
paras = soup.find_all('p')
# print(paras)

# Get all the anchor tags from the page
anchor = soup.find_all('a')
# print(anchor)


# Get first element - 
# print(soup.find('p'))

# Get class of element - 
# print(soup.find('p')['class'])


# Find all the elemment with class "lead" -
# print(soup.find_all('p',class_="lead"))

# Get the text from tags -
# print(soup.find('p').get_text())

# Get text from full html page -
# print(soup.get_text())




# How to get all links from page and print them -
all_links = set()
for link in anchor:
    if (link.get('href'))!="#" :
        link_text = "https://www.codewithharry.com"+link.get('href')
        all_links.add(link_text)
for item in all_links:
    # print(item)
    pass


#  Comments - 
markup = "<p><!-- This is a html comment --></p>"
soup2 = BeautifulSoup(markup)
# print(soup2.p)
# print(soup2.p.string)
# print(type(soup2.p.string))


navbarSupportedContent = soup.find(id="navbarSupportedContent")
# print(navbarSupportedContent.contents)

# .contents - A tag's children are available in a list
# .children - A tag's children are available in as a genrator


for element in navbarSupportedContent.contents :
    # print(element)
    pass

# It will print all items in navbarSupportedContent
for items_12 in navbarSupportedContent.strings :
    # print(items_12)
    pass

# It will beautify and print all items in navbarSupportedContent
for items_123 in navbarSupportedContent.stripped_strings :
    # print(items_123)
    pass

# For printing parent of any tag -
# print(navbarSupportedContent.parent)


# For genrating parent of any tag
for parentsin in navbarSupportedContent.parents :
    # print(parentsin)
    # print(parentsin.name)
    pass

# To print next sibling -
# print(navbarSupportedContent.next_sibling.next_sibling)

# To print previous sibling -
# print(navbarSupportedContent.previous_sibling.previous_sibling)


# CSS selecter - 
ele = soup.select('#loginModal')
print(ele)

# Class selecter -
ele_1 = soup.select('.loginModal')
print(ele)








