from scraping.website_scraper import WebsiteScraper

ws = WebsiteScraper()
ws.set_url('http://worldtimeapi.org/api/ip')
res = ws.get_request_json()
print(res)
