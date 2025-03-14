import requests

url = "https://jko-backend.vercel.app/send-email"

data = {"name":"Mauricio", "email":"mauricio@gmail.com", "message":"sent from client!!"}
response = requests.post(url, json=data)

print(response.text)
print(response.status_code)
