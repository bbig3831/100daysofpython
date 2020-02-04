import json
import requests
from pprint import pprint

with open('mount-data.json', 'r') as my_file:
    data = json.loads(my_file.read())

for item in data.items():
    pprint(item)

is_flying = []
for mount in data['mounts']['collected']:
    if mount['isFlying']:
        is_flying.append(mount)

print(len(is_flying))
