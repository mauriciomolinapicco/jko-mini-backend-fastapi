import requests

url = "https://jko-backend.vercel.app/"

response = requests.get(url)

print(response.text)
print(response.status_code)
