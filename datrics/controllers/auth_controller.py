import requests

from datrics.services.storage_service import StorageService
from datrics.services.show_message import show_error, show_message
from datrics.constants.links import AUTH_SIGN_IN_URL


class AuthController:

    @staticmethod
    def login(email, password):
        data = {
            'email': email,
            'password': password,
        }
        try:
            response = requests.post(url=AUTH_SIGN_IN_URL, data=data)

            if response.status_code == requests.codes.ok:
                response_data = response.json()
                access_token = response_data.get('accessToken', '')
                StorageService.save_token(access_token)
                show_message('Successfully logged in')
            elif response.status_code == requests.codes.unauthorized:
                AuthController.logout()
            else:
                show_error("Can't sign in. Email or password are incorrect")
        except Exception as e:
            show_error(e)

    @staticmethod
    def logout():
        StorageService.remove_token()
