import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgxNDQ1MjQxLCJqdGkiOiIwYzRjODI4YWI3NjI0YWM3YmIxNTNiMjM5MzMwZDUwNSIsInVzZXJfaWQiOjF9.gXV6wLdv64-avquFut_J9cJj83u9YUYLQ8Btp6jlZlg'

r = requests.get('http://127.0.0.1:8000/paradigms', headers=headers)

print(r.text)
