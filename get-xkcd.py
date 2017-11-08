import json
import urllib.request
import ssl
from sys import argv

unverified = ssl._create_unverified_context()

start = 614
end = 617

# last comic with a reliable transcript is roughly 1608?
# Last with any might be 1677.
# But 1677 really contains transcript from 1674.
# someone noticed this: http://forums.xkcd.com/viewtopic.php?t=113433

print(argv)
if len(argv) == 3:
    s = int(argv[1])
    e = int(argv[2])
    assert s < e
    start = s
    end = e + 1

def get_comic_by_num(n):
    url = 'https://xkcd.com/' + str(n) + '/info.0.json'
    response = urllib.request.urlopen(url, context = unverified)
    json_data = str(response.read(), encoding='utf-8')
    return json.loads(json_data)

print("comic_num,panels,words")

for comic_to_get in range(start, end):
    if comic_to_get == 404:
        next
    python_obj = get_comic_by_num(comic_to_get)
    n = python_obj['num']
    assert comic_to_get == n
    T = python_obj['transcript']
    panels = len(T.split('\n\n')) - 1
    words = len(T.split())
    print(str(n) + ',' + str(panels) + ',' + str(words))
