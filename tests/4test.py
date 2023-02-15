import requests

import json

baseURL = 'https://petstore.swagger.io/v2'
user1 ="user1"
user2 ="user2"

data = {
  "id": 0,
  "username": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}




headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Host': 'petstore.swagger.io',
    'Content-Length': '236',
    'Cache-Control': 'no-cache'
}

res = requests.post(f"{baseURL}/user", headers=headers, data=json.dumps(data))
print(res.status_code)
print('Код ответа - 200 \nСоздан пользователь:')

print(res.json())
#user_id = dict(res.json())['id']

data["username"]= "user1"
data["username"]= "user2"
print(f'\nменяем имя пользователя на {"user2"}')

res2 = requests.put(f"{baseURL}/user", headers=headers, data=json.dumps(data))
print(res2.status_code)
print('Код ответа - 200 \nВнесены изменения:')

print('\nЗапрашиваем данные с сервера о пользователе по "username" -'+str("username"))
res3=requests.get(f"{baseURL}/user/{user1}", headers=headers)

print(res3.status_code)
print('Код ответа - 200 \nНа сервере имеются данные:')

print('\nУдаляем данные о пользователе по username -'+str("username"))
res4=requests.delete( f"{baseURL}/user/{user1}", headers=headers)

print(res4.status_code)
print('Код ответа - 200 \nДанные о пользователе удалены:')

print('\nЗаново запрашиваем данные с сервера о пользователе по username -'+str(user2))
res5=requests.get( f"{baseURL}/user/{user2}", headers=headers)

print(res5.status_code)
print('Код ответа - 200 На сервере имеются данные, Код ответа - 404 Данных нет')
