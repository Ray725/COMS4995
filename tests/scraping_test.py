from scraping.art_of_war import ArtOfWar
from scraping.website_scraper import WebsiteScraper

class TestScraping:
    def test_website_scraper_url_default(self):
        ws = WebsiteScraper(None)
        assert ws.get_request_raw_text(None) is None

    def test_website_scraper_set_url(self):
        ws = WebsiteScraper(None)
        ws.set_url('test_url')
        assert ws.url == 'test_url'

    def test_aow_scraper_is_proper_subclass(self):
        aow = ArtOfWar()
        aow.set_url('test_url')
        assert aow.url == 'test_url'
