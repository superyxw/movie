from bs4 import BeautifulSoup
import re

patternStr = r'\s*导演: (.*?)\s{3}'
p = re.compile(patternStr)

class HtmlParser(object):

    def __init__(self,url):
        self.url = url;

    def parser_html(self,html):
        soup = BeautifulSoup(html, 'lxml');
        movie_infos = []
        movie_lists = soup.select(".grid_view li")
        for movie_item in movie_lists:
            movie_name = movie_item.find('span',class_='title').getText()
            movie_director = re.match(p,movie_item.select('div.bd p')[0].getText()).group(1)
            movie_infos.append(list((movie_name,movie_director)))
        next_page = soup.find('span', class_='next').find('a')
        if next_page:
            return movie_infos, self.url + next_page['href']
        return movie_infos, None
