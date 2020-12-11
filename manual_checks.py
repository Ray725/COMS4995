from scraping.art_of_war import ArtOfWar
from scraping.project_gutenberg import ProjectGutenberg
from formatting.format_helper import format_message

'''
aow = ArtOfWar()
res = aow.search_word('temper')
print(res)
'''

pg = ProjectGutenberg()
book = pg.search_book('the republic')

res = pg.search_text('trust')

telegram_message = format_message('the republic', book, res)
print(telegram_message)
