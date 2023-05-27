import pandas as pd

naruto = pd.read_html('https://en.wikipedia.org/wiki/Naruto_(season_1)')

print(len(naruto))

print(naruto[1])