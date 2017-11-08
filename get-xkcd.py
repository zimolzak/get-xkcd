import json
import urllib.request
import ssl
from sys import argv

comic_to_get = 615
if len(argv) > 1:
    comic_to_get = int(argv[1])

def get_comic_by_num(n):
    url = 'https://xkcd.com/' + str(comic_to_get) + '/info.0.json'
    unverified = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context = unverified)
    json_data = str(response.read(), encoding='utf-8')
    return json.loads(json_data)

python_obj = get_comic_by_num(comic_to_get)

#print(json.dumps(python_obj, sort_keys=True, indent=4))
#print(python_obj.keys())
# usu keys:
# safe_title link alt news title num transcript month day img year

n = python_obj['num']
assert comic_to_get == n

T = python_obj['transcript']
L = T.split('\n\n')
print("Comic " + str(n) + "\tEst. num. of panels:", len(L) - 1)
