import requests
import json

if __name__ == '__main__':
    url = 'https://stage.api.enviame.io/api/s2/v2/companies/620/deliveries'
    payload = { 'identifier' : '1549126'}
    headers = { 'Content-Type': 'application/json', 'Accept' : 'application/json' , 'api-key' : '798171c39baf6fd212aaacacc5793b8e'}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response)
    if response.status_code == 200:
        content = response.content
        print(response.content)
        file = open('enviame.json', 'wb')
        file.write(content)
        file.close()