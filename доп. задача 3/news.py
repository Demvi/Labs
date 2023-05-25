import re 
from functools import reduce 
from collections import OrderedDict

news = []

with open('news.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    match = re.match(r'^(\d+)\s(.+)$', line)
    if match:
        news.append((int(match.group(1)), match.group(2)))

positive_news = reduce(lambda x, y: x + [y] if y[0] > x[-1][0] else x, news[1:], [news[0]])

for news in positive_news:
    print(news[1])