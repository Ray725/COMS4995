'''Class meant to be used to interface with suntzusaid.com.
'''
from bs4 import BeautifulSoup
from scraping.website_scraper import WebsiteScraper

class ArtOfWar(WebsiteScraper):
    '''A class intended to be used as an API for suntzusaid.com.
    '''
    def __init__(self, url=None):
        if url is None:
            super().__init__('https://suntzusaid.com/')

    def search_word(self, word):
        '''Gets the contents of the /search.php?q={word} endpoint.

        Args:
            word: keyword to investigate.

        Returns:
            List of tuples of (passage quote, relevant passage URL route).
        '''
        if len(word) == 0:
            return []

        route = f'search.php?q={word}'

        res = self.get_request_raw_text(self.url + route)
        soup = BeautifulSoup(res, 'html.parser')
        search_results = soup.find_all(class_='searchresult')

        if search_results == []:
            return []

        parsed_results = []
        for result in search_results:
            snippet = result.text.split(' ss. ')[0]
            parsed_results.append((snippet, result.a.get('href')))

        return parsed_results

    def parse_book(self, book_route):
        '''Takes in a route for a book route (e.g. book/6/33/) and
        returns the text of the webpage.

        Args:
            book_route: string that denotes a book passage route

        Returns:
            Raw text, perhaps separated into a list?
        '''
        return self.url + book_route
