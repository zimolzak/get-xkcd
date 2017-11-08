import json
import urllib.request
import ssl
from sys import argv

comic_to_get = 615
if len(argv) > 1:
    comic_to_get = int(argv[1])

url = 'https://xkcd.com/' + str(comic_to_get) + '/info.0.json'
unverified = ssl._create_unverified_context()
response = urllib.request.urlopen(url, context = unverified)
json_data = str(response.read(), encoding='utf-8')
python_obj = json.loads(json_data)

#print(json.dumps(python_obj, sort_keys=True, indent=4))
#print(python_obj.keys())
# usu keys:
# safe_title link alt news title num transcript month day img year

T = python_obj['transcript']
L = T.split('\n\n')
print(T)

print("\nEst. num. of panels:", len(L) - 1)
n = python_obj['num']
if comic_to_get == n:
    print("Key 'num' looks ok.")
else:
    print("\n*** Key 'num' is " + str(n) + ": DOES NOT match comic_to_get.")
