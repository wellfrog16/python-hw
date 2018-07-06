# encoding:utf-8

from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title qq op"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">链接1</a>,
<a href="http://example.com/lacie" class="sister" id="link2">呵呵2</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie哦哦</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

print u'所有链接'

links = soup.find_all('a')
for link in links:
    print link.name, link['href'], link.get_text()


print u'指定链接'
node = soup.find('a', href='http://example.com/tillie')
print node.name, node['href'], node.get_text()

print u'正则匹配'
node = soup.find('a', href=re.compile(r'ill'))
print node.name, node['href'], node.get_text()

print u'段落文字'
node = soup.find('p', class_='title')
print node.name, node['class'], node.get_text()