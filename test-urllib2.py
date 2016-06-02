#!/usr/bin/env python
# coding=utf-8
import urllib2, cookielib

url = "http://www.d4smart.com"

print 'Method 1'
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print 'Method 2'
request = urllib2.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print 'Method 3'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
# print len(response3.read())
print response3.read()

