import requests

class HtmlGet:

    def download_page(self,url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
        data = requests.get(url, headers=headers).text
        return data



if __name__ == '__main__':
    pass