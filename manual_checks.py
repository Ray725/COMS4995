from scraping.art_of_war import ArtOfWar
from scraping.project_gutenberg import ProjectGutenberg

'''
aow = ArtOfWar()
res = aow.search_word('temper')
print(res)
'''

pg = ProjectGutenberg()
res = pg.search_book('the republic')
print(res)

res = pg.search_text('trust')
print(res)
print(len(res))
