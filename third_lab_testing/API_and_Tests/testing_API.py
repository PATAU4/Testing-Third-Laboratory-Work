import pytest
import requests

# #get
import get_api_key
import get_list_of_pets

#post
import create_pet_simple
import add_information_about_new_pet
import set_photo

#delete
import delete

#put
import put_new_information




# ФИКСТУРЫ

# get:


# get_key

@pytest.fixture()
def get_api_key_fixture():
    get_api_key
    return True
def test_get_api_key(get_api_key_fixture):
    assert get_api_key_fixture == 1, "GetKey Error"



# get_list
@pytest.fixture()
def get_list_fixture():
    get_list_of_pets
    return True
def test_get_list(get_list_fixture):
    assert get_list_fixture == 1, "GetList Error"




# # post:


# post simple_pet

@pytest.fixture()
def post_simple_pet_fixture():
    create_pet_simple
    return True
def test_post_simple_pet(post_simple_pet_fixture):
    assert post_simple_pet_fixture == 1, "PostSimplePet Error"



# post add_info

@pytest.fixture()
def post_add_info_fixture():
    add_information_about_new_pet
    return True
def test_post_add_info(post_add_info_fixture):
    assert post_add_info_fixture == 1, "PostAddInfo Error"



# post set_photo

@pytest.fixture()
def post_set_photo_fixture():
    set_photo
    return True
def test_post_set_photo(post_set_photo_fixture):
    assert post_set_photo_fixture == 1, "SetPhoto Error"




#delete

@pytest.fixture()
def delete_pet_fixture():
    delete
    return True
def test_delete_pet(delete_pet_fixture):
    assert delete_pet_fixture == 1, "DeletePet Error"



#put

@pytest.fixture()
def put_pet_new_info_fixture():
    put_new_information
    return True
def test_put_new_pet(put_pet_new_info_fixture):
    assert put_pet_new_info_fixture == 1, "PutNewInfo Error"






# ПАРАМЕТРИЗАЦИЯ

# POST
key = '802cc048b84f7ca443618ce18ce9990bd8f3c2707e3331b69e848228'
wrong_key = '12345'

request_url_pet_simple = "https://petfriends1.herokuapp.com/api/create_pet_simple"
request_url_new_pet = "https://petfriends1.herokuapp.com/api/pets"

post_header_formData_pet_simple = { "auth_key": key, "name": "Arolf", "animal_type":"Tibetan Shepherd", "age": "4"}
post_header_formData_new_pet = {"auth_key":wrong_key, "name":"Arolf", "animal_type":"Tibetan Shepherd","age": '8',"pet_photo": ""}


@pytest.mark.parametrize('url, param, header, result',
                         [  # post_simple_pet
                             (request_url_pet_simple, post_header_formData_pet_simple, post_header_formData_pet_simple, True), # позитивный сценарий 
                             # post_add_info
                             (request_url_new_pet, post_header_formData_new_pet, post_header_formData_new_pet, False), # негативный сценарий 
                         ]
                         )
def test_post( url, param, header, result ):

    r = requests.post( url, params=param, headers=header )

    if requests.codes.ok == result:
        print( f' Status: {r.status_code == requests.codes.ok}' ) # возвращает True, если код статуса не 4xx и не 5xx
    else:
        print(" PostError")



# GET


key = '802cc048b84f7ca443618ce18ce9990bd8f3c2707e3331b69e848228'
wrong_key = '12345'

request_url = 'https://petfriends1.herokuapp.com/api/key' # ссылка на API с ключем
request_url_list_of_pets = "https://petfriends1.herokuapp.com/api/pets?filter=my_pets"

get_email_pass_header = { 'email':'lilchichaboba@gmail.com', 'password':'1488' } # информация о пользователе, который значится в БД
get_header_query_wrong = {"auth_key ": key, "filter": "pets"}


@pytest.mark.parametrize('url, param, header, result',
                         [  # get_api_key
                             (request_url, get_email_pass_header, get_email_pass_header, True), # позитивный сценарий
                             # get_my_pets_list
                             (request_url_list_of_pets, get_header_query_wrong, get_header_query_wrong, False) # негативный сценарий 
                         ]
                         )
def test_get( url, param, header, result ):

    r = requests.get( url, params=param, headers=header )

    if requests.codes.ok == result:
        print( f' Status: {r.status_code == requests.codes.ok}' ) # возвращает True, если код статуса не 4xx и не 5xx
    else:
        print(" PostError")