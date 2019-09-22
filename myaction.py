#!/usr/bin/python

import writer
import os
import datetime

myfile = datetime.datetime.now().strftime("%d-%m-%Y-%s")
myindex = "index.html"
new = writer.Operations(myfile)

filelocation = os.path.join('/var/www/html/myblog', myfile)
indexlocation = os.path.join('/var/www/html/myblog', myindex)

new.CreateFile(filelocation)
new.IndexFile(indexlocation)

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<meta http-equiv="Refresh" content="0;'
print 'url=http://192.168.56.35/myblog/index.html">'
print '</head>'
print '<body>'
print '</body>'
print '</html>'
