from collections import Counter
from datetime import datetime
import re

import feedparser
import plotly
import plotly.graph_objs as go
from plotly.offline import plot

blog_feed = feedparser.parse('http://projects.bobbelderbos.com/pcc/dates/all.rss.xml')
entries = blog_feed['entries']


def get_year_month(date_str):
    date_str = date_str.split('+')[0].strip()
    dt = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S')
    return f'{dt.year}-{dt.month}'

def get_category(link):
    known = {
        'codechallenge':'challenge',
        'twitter':'news',
        'special':'special',
        'guest':'guest'
    }
    default = 'article'
    category = re.sub(r'.*\.es/([a-z]+).*', r'\1', link)
    return known.get(category) or default

def transpose_list_of_tuples(data):
    if isinstance(data, dict):
        data = data.items()

    transposed = list(zip(*data))
    return transposed

pub_dates = [get_year_month(entry['published']) for entry in entries]
posts_by_month = Counter(pub_dates)
x, y = transpose_list_of_tuples(posts_by_month)
data = [go.Bar(x=x, y=y)]
plot(data, filename='post-frequency.html')

categories = [get_category(entry['link']) for entry in entries]
cnt = Counter(categories)
categories = cnt.most_common()
labels, values = transpose_list_of_tuples(categories)
pie = go.Pie(labels=labels, values=values)
plot([pie], filename='categories.html')

tags = [tag.term.lower() for entry in entries for tag in entry.tags]
cnt = Counter(tags)
top_tags = cnt.most_common(10)
labels, values = transpose_list_of_tuples(top_tags)
tags = go.Pie(labels=labels, values=values)
plot([tags], filename='tags.html')

