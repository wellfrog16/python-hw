# encoding:utf-8

class UrlManager(object):
    def __init__(self):
        self.newUrls = set()
        self.oldUrls = set()

    def add(self, url):
        if url is None:
            return
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url)

    def adds(self, urls):
        if urls is None or len(urls) == 0:
            return

        for url in urls:
            self.add(url)

    def hasNew(self):
        return len(self.newUrls) != 0

    def getNewUrl(self):
        url = self.newUrls.pop()
        self.oldUrls.add(url)
        return url