
import requests

value = 'Token  9e998634d347cd3ab7fbc03973e0318fda6f42dd'
body_val = {
    "name": "Java",
    "author": "XXX33",
    "price": 22934.3,
    "qty": 203,
    "publication": "TTTT",
    "reviews": "stars"
}
response = requests.post('http://localhost:8000/v1/book/',
                         headers={'Authorization':value},json=body_val)
print(response.status_code)
print(response.json())