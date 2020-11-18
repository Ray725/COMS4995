'''Class meant to interact with Project Gutenberg.
'''
from bs4 import BeautifulSoup
from scraping.website_scraper import WebsiteScraper

class ProjectGutenberg(WebsiteScraper):
    '''Class meant to be used as an API for Project Gutenberg.
    '''
    def __init__(self, url=None):
        gurl = 'https://www.gutenberg.org/ebooks/search/?query='
        if url is None:
            super().__init__(gurl)
        self.book = None
        self.book_html = None

    def search_text(self, query_string):
        '''Assumes a book has already been searched for and set.
        Returns the instances of the query_string in the book.

        Args:
            query_string: query string such as "governance"

        Returns: list of text snippets from the book which contain
        the query string
        '''
        if self.book_html is None:
            return None

        res = self.get_request_raw_text(self.book_html)
        soup = BeautifulSoup(res, 'html.parser')
        paragraphs = soup.findAll('p')
        search_results = []
        for paragraph in paragraphs:
            if query_string in paragraph.text:
                stripped = ' '.join(paragraph.text.split())
                search_results.append(stripped)

        return search_results

    def search_book(self, query_string):
        '''Takes in a space-separated query string to find a desired
        book or author. Returns the URL of the first result and its
        HTML page of text. Assumes that each book has an HTML format
        available on Project Gutenberg.

        Args:
            query_string: query string such as "thoreau" or "the republic"

        Returns:
            URL string of the corresponding book and HTML page
        '''
        if len(query_string) == 0:
            return None

        search_url = self.url + query_string.replace(' ', '+')
        res = self.get_request_raw_text(search_url)
        soup = BeautifulSoup(res, 'html.parser')
        book_results = soup.findAll('li', {'class': 'booklink'})

        if len(book_results) == 0:
            return None

        top_result = book_results[0]
        href = top_result.find('a')['href']
        self.book = 'https://www.gutenberg.org' + href

        book_res = self.get_request_raw_text(self.book)
        book_soup = BeautifulSoup(book_res, 'html.parser')
        rows = book_soup.findAll('tr', {'class': 'even'})

        if len(rows) == 0:
            return None

        self.book_html = rows[0]['about']

        return self.book_html
