import re
import urllib.request
from bs4 import BeautifulSoup
import os

def getHtml(url):
  with urllib.request.urlopen(url) as response:
        html = response.read()
  return html.decode('utf-8')


url = "http://wufazhuce.com/article/2000"
html = getHtml(url)

file = open("content.txt", "w+")
soup = BeautifulSoup(html, "html5lib")
print("title", file=file)  
print(soup.head.title.string, file=file)
print("author", file=file)
print(soup.p.string.rstrip(), file=file)

 
context_image = soup.find(attrs={"class": "articulo-contenido"})

first_tag = context_image.img
while (first_tag != None)
	tag = soup.new_tag("a")
	tag.string = first_tag.attrs["src"]
	first_tag.insert_before(tag)
	first_tag = first_tag.find_next_sibling("img")


print(context_image.get_text(), file=file)

