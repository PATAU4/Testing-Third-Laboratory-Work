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

delete_header_path = {"auth_key": key, "pet_id": pet_id}

request_url = "https://petfriends1.herokuapp.com/api/pets/" + pet_id

def delete( url, param, header ):
    r = requests.delete(url, params=param, headers=header )

    if r.status_code == requests.codes.ok:
        print( f'\n Status-Code: {r.status_code}' ) # принтит статус 
        print( f' Status: {r.status_code == requests.codes.ok}' ) # возвращает True, если код статуса не 4xx и не 5xx
        print(' Питомец был удален')
    else:
        print(" PostError") 



delete_pet = delete( request_url, delete_header_path, delete_header_path)