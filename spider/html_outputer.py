# encoding:utf-8

class HtmlOutputer:
    def __init__(self):
        self.datas = []

    def collect(self, data):
        if data is None:
            return
            
        self.datas.append(data)

    def html(self):
        fout = open('output.html', 'w')

        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</td>')

        fout.write('</table>')
        fout.write('</table>')
        fout.write('</body>')
        fout.close()