# encoding:utf-8
import urllib2
import cookielib
import sys

url = 'http://www.swiper.com.cn/'
type = sys.getfilesystemencoding()

# 1
print u'''----------------\n1一\n----------------'''
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

# 2
print u'''----------------\n2二\n----------------'''
request = urllib2.Request(url)
request.add_header('user-agent', 'Mozilla/5.0')
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

# 3
print u'''----------------\n3三\n----------------'''
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
print response3.read().decode("UTF-8").encode(type)