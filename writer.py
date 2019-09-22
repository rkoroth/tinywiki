#!/usr/bin/python

import cgi, cgitb
import os


class Operations:
        
    form = cgi.FieldStorage()
    formdata = form.getvalue('data')
    formhead = form.getvalue('heading')
    header = "<html> <body>"
    footer = "</body> </html>"
    head = "<h1>" + formhead + "</h1>"
    data = "<p>" + formdata + "</p>"
    filedata = header + head + data + footer

    indexpre = "<p><a href=\""
    indexpre2 = "\">"
    indexpost = "</a></p>"
    
    def __init__(self, myfile):
        self.myfile = myfile
	self.link = myfile + " :- " + self.formhead 
    
    def CreateFile(self, filelocation):
        fd = open(filelocation, "a+")
        fd.write("%s\n" % (self.filedata))
        fd.close()

    def IndexFile(self, indexlocation):
        indexdata = self.header + self.indexpre + self.myfile + self.indexpre2 + self.link + self.indexpost + self.footer
        fd = open(indexlocation, "a+")
        fd.write("%s\n" % (indexdata))
        fd.close()
