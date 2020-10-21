'''File containing WebsiteScraper class.
'''
import requests

class WebsiteScraper:
    '''Used as superclass for classes which use webscraping.
    '''
    def __init__(self, url):
        self.set_url(url)

    def set_url(self, url):
        '''Sets the url of this object. Used as base url for the requests
        made by this class.

        Args:
        '''
        self.url = url

    def get_request_raw_text(self, url):
        '''Returns the raw text of a website.

        Args:
            url: url string
        '''
        if url is None or len(url) == 0:
            return None

        res = requests.get(url)

        if res.status_code == 200:
            return res.text
        print('Request GET error:', res.status_code)
        return self.get_request_raw_text(url)
