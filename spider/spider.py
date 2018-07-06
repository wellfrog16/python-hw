# encoding:utf-8
import url_manager, html_download, html_parser, html_outputer

class Spider(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_download.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, url):
        count = 1
        self.urls.add(url)
        while self.urls.hasNew():
            try:
                newUrl = self.urls.getNewUrl()
                print 'craw %d : %s' % (count, newUrl)
                content = self.downloader.download(newUrl)
                urls, data = self.parser.parse(newUrl, content)
                self.urls.adds(urls)
                self.outputer.collect(data)

                if count == 10:
                    break
                    
                count = count + 1
            except:
                print 'error'

        self.outputer.html()

if __name__=='__main__':
    rootUrl = 'https://baike.baidu.com/item/python/407313'
    spider = Spider()
    spider.craw(rootUrl)
