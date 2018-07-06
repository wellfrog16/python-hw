# encoding:utf-8

from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
    def parse(self, url, content):
        if url is None or content is None:
            return

        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        urls = self.getUrls(url, soup)
        data = self.getData(url, soup)

        return urls, data

    def getUrls(self, page, soup):
        urls = set()

        links = soup.find_all('a', href=re.compile(r'/item/'))
        for link in links:
            url = link['href']
            # 此处会自动处理url域名
            newUrl = urlparse.urljoin(page, url)
            urls.add(newUrl)

        return urls

    def getData(self, page, soup):
        res = {}

        res['url'] = page

        #<dd class="lemmaWgt-lemmaTitle-title">
        titleNode = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res['title'] = titleNode.get_text()

        summaryNode = soup.find('div', class_='lemma-summary')
        res['summary'] = summaryNode.get_text()
        
        return res
    
        
