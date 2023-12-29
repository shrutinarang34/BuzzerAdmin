import core
def user_login(username: str, password: str, business_id: int):
    data = {
        'email': username,
        'password': password,
        'business_id': business_id

    }
    response =  core.post(core.endpoints('login'), json = data)
    print(response)
