import feedparser
import sys
url=sys.argv[1]

for i in feedparser.parse(url).entries:
    print(i.title)
