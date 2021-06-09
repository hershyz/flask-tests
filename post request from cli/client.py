import requests

# convert payload args into json
payload = {"name": "Daby", "mylist": ["one", "two", "three"]}
r = requests.post("http://127.0.0.1:5000/post_req", json=payload)
print(r.text)