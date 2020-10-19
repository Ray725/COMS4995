import requests

class WebsiteScraper:
    def __init__(self, url):
        self.set_url(url)

    def set_url(self, url):
        self.url = url

    def get_request_raw_text(self, url):
        if url is None or len(url) == 0:
            return None

        res = requests.get(url)

        if res.status_code == 200:
            return res.text
        else:
            print('Request GET error:', res.status_code)
            return
