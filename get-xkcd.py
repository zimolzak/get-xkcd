import json
import urllib.request
import ssl

unverified = ssl._create_unverified_context()

def get_comic_by_num(n):
    url = 'https://xkcd.com/' + str(n) + '/info.0.json'
    response = urllib.request.urlopen(url, context = unverified)
    json_data = str(response.read(), encoding='utf-8')
    return json.loads(json_data)

#### main ####

print("comic_num,panels,words")

comic_to_get = 615
python_obj = get_comic_by_num(comic_to_get)
n = python_obj['num']
assert comic_to_get == n
T = python_obj['transcript']
panels = len(T.split('\n\n')) - 1
words = len(T.split())
print(str(n) + ',' + str(panels) + ',' + str(words))
