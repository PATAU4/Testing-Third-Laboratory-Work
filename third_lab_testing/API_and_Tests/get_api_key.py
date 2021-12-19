import requests # вся работа осуществляется с помощью библиотеки requests
import json

request_url = 'https://petfriends1.herokuapp.com/api/key' # ссылка на API с ключем
get_email_pass_header = { 'email':'lilchichaboba@gmail.com', 'password':'1488' } # информация о пользователе, который значится в БД

def get_API_key( url, header ): # функция получения ключа API, он необходим для реализации других методов API
    r = requests.get( url, headers=header ) # информация о пользователе должна передаваться в headers, email и password

    print( f' Status-Code: {r.status_code}' ) # принтит статус 
    print( f' Status: {r.status_code == requests.codes.ok}' ) # возвращает True, если код статуса не 4xx и не 5xx

    # здесь я реализовал бешенный парсинг полученного ключа, он и передается в return

    templates = r.text # получаем ключ с помощью метода .text

    dict_key = json.loads(templates)
    key = dict_key['key']

    print(f' Earned key: {key}')
    return key


get_key = get_API_key( request_url, get_email_pass_header )

# print(get_API_key( request_url, email_pass_header )) 