import requests
from bs4 import BeautifulSoup


class Website:
    headers = { 
        'User-Agent':  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }   
    def __init__(self, url):
        self.url = url 
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(['script', 'style', 'img', 'input']):
            irrelevant.decompose()
        self.text = soup.body.get_text()


class WikiWebsite:
    headers = { 
        'User-Agent':  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }   
    def __init__(self, url):
        self.url = url 
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(['script', 'style', 'img', 'input']):
            irrelevant.decompose()
        self.text = soup.body.get_text()
        paragraphs = soup.select("div.mw-parser-output > p")

        all_paras = []
        for para in paragraphs:
            if para.text.strip():
                all_paras.append(para.text.strip())

        if len(all_paras) == 0:
            self.main_text = "No content found."
        else:
            self.main_text = '\n\n'.join(all_paras)


