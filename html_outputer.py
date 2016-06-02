#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup

class HtmlOutputer(object):

    def __init__(self):
        self.file = "output.html"
        self.datas = []
    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def _prettify(self):
        fin = open(self.file, 'r')
        str = fin.read().decode('utf-8')
        fin.close()
        fout = open(self.file, 'w')

        soup = BeautifulSoup(str, 'html.parser', from_encoding='utf-8')
        cont = soup.prettify()
        fout.write(cont.encode('utf-8'))
        fout.close()

    def output_html(self):
        fout = open(self.file, 'w')

        fout.write("<html>")
        fout.write("<head>")
        fout.write('<meta charset="utf-8" />')
        fout.write("</head>")
        fout.write("<body>")
        fout.write('<table border="1">')

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()
        self._prettify()
