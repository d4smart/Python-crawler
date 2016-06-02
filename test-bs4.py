#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup
import urllib2

url = "http://volunteer.hust.edu.cn"
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

request = urllib2.urlopen(url)
html_doc = request.read()
soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

print 'Links'
a = 1
links = soup.find_all('a')
for link in links:
    print a, ": ", link.name, link['href'], link.get_text()
    a = a+1
