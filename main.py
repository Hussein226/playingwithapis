import requests as r


print("calling ap")

api ="https://api.publicapis.org/entries"

response = r.get(api).json()

for data in response["entries"]:
    print(data["API"])


