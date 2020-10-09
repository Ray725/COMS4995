import requests

class WebsiteScraper:
    def __init__(self):
        pass

    def set_url(self, url):
        self.url = url

    def get_request_json(self):
        try:
            url = self.url
        except AttributeError:
            print('Invalid method call, url is undefined')
            return

        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            print('Request GET error:', res.status_code)
            return
