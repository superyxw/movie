from HtmlGet import HtmlGet
from HtmlParser import HtmlParser

URL='https://movie.douban.com/top250'
outputMode= "{0:{2}^20}\t{1:^10}"

htmlGet = HtmlGet()

htmlParser = HtmlParser(URL)

url = URL

while url:
    infos,url = htmlParser.parser_html(htmlGet.download_page(url))
    for info in infos:
        print(outputMode.format(info[0],info[1],chr(12288)))