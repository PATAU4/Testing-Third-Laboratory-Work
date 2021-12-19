import get_api_key
import get_list_of_pets
import requests

key = (get_api_key.get_key) # получение ключа 

dct = get_list_of_pets.get_list

# name_of_pet = str(input('Введите имя питомца:\n'))
# нереально сильно запарсил id питомца 

for i in range( len(dct[0]) ): # необходимо указывать имя питомца в ручную в коде, либо использовать инпут
    if dct[0][i]['name'] == 'Arolf':
        pet_id = dct[0][i]['id'] 

put_header_path_formData = { "auth_key": key, "pet_id": pet_id, "name": "Arolf Renamed", "animal_type":"Tibetan Shepherd", "age": "4" }

request_url = "https://petfriends1.herokuapp.com/api/pets/" + pet_id

def rename( url, param, header ):
    r = requests.put(url, params=param, headers=header )

    if r.status_code == requests.codes.ok:
        print( f'\n Status-Code: {r.status_code}' ) # принтит статус 
        print( f' Status: {r.status_code == requests.codes.ok}' ) # возвращает True, если код статуса не 4xx и не 5xx
        print(' Питомец был переименован')
    else:
        print(" PostError") 


put_new_info = rename( request_url, put_header_path_formData, put_header_path_formData)