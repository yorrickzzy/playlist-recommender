import requests

url = "http://localhost:52011/api/recommend"
data = {"songs": ["Humble", "DNA"]}

response = requests.post(url, json=data)
print(response.json())  
