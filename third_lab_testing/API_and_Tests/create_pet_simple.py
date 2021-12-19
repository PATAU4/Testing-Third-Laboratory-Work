import get_api_key
import requests


key = (get_api_key.get_key) # получение ключа 

get_header_formData = { "auth_key": key, "name": "Arolf", "animal_type":"Tibetan Shepherd", "age": "4"}

request_url = "https://petfriends1.herokuapp.com/api/create_pet_simple"


def create_pet_simple( url, param, header ):

    r = requests.post( url, params=param, headers=header )

    if r.status_code == requests.codes.ok:
        print( f'\n Status-Code: {r.status_code}' ) # принтит статус 
        print( f' Status: {r.status_code == requests.codes.ok}' ) # возвращает True, если код статуса не 4xx и не 5xx
        print(f'\n Sucsess!\n Name: {get_header_formData["name"]}\n Animal Type: {get_header_formData["animal_type"]}\n Age: {get_header_formData["age"]}')
    else:
        print(" PostError")


post_create_pet_simple = create_pet_simple( request_url, get_header_formData, get_header_formData)