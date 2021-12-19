import get_api_key
import get_list_of_pets
import requests

key = (get_api_key.get_key) # получение ключа 

dct = get_list_of_pets.get_list

# name_of_pet = str(input('Введите имя питомца:\n'))

# нереально сильно запарсил id питомца 

for i in range( len(dct[0]) ):
    if dct[0][i]['name'] == 'Arolf':
        pet_id = dct[0][i]['id'] 


post_header_path_formdata = { "auth_key": key, "pet_id":pet_id }


request_url = "https://petfriends1.herokuapp.com/api/pets/set_photo/" + pet_id


def set_photo(url, post_params, post_headers):

    r = requests.post(url, params=post_params, headers=post_headers, files={"pet_photo": open('pepe.jpg', 'rb')})

    if r.status_code == requests.codes.ok:
        print( f'\n Status-Code: {r.status_code}' ) # принтит статус 
        print( f' Status: {r.status_code == requests.codes.ok}' ) # возвращает True, если код статуса не 4xx и не 5xx
    else:
        print(" PostError")


post_set_photo = set_photo( request_url, post_header_path_formdata, post_header_path_formdata )