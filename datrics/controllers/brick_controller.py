import tarfile
import requests
import pathlib
import os

from datrics.controllers.auth_controller import AuthController
from datrics.services.storage_service import StorageService
from datrics.services.brick_service import BrickService
from datrics.services.show_message import (
    show_error,
    show_message,
)
from datrics.constants.links import (
    POST_PROJECT_BRICKS_URL,
    PATCH_PROJECT_BRICK_URL,
    DELETE_PROJECT_BRICK_URL,
)


class BrickController:

    @staticmethod
    def push(brick_directory):
        project_id = StorageService.get_project_id(brick_directory)
        brick_id = StorageService.get_brick_id(brick_directory)

        if brick_id:
            BrickController.update(brick_directory, project_id, brick_id)
        else:
            BrickController.create(brick_directory, project_id)


    @staticmethod
    def create(brick_directory, project_id):
        brick_file_path = BrickService.pack_brick(brick_directory)
        token = StorageService.get_token()
        params = {
            'token': token
        }

        try:
            files = {'upload': open(brick_file_path, 'rb')}
            url = POST_PROJECT_BRICKS_URL.replace(':project_id', project_id)
            response = requests.post(url=url, files=files, params=params)

            if response.status_code == requests.codes.ok:
                show_message('Brick successfully added!')
                brick_id = str(response.json()['brick']['id'])
                StorageService.save_brick_id(brick_directory, brick_id=brick_id)
            elif response.status_code == requests.codes.unauthorized:
                AuthController.logout()
                show_error("Please log in to push brick")
            else:
                show_error("Can't create brick")
        except Exception as e:
            show_error(e)
        finally:
            BrickService.remove_brick_file(brick_file_path)

    @staticmethod
    def update(brick_directory, project_id, brick_id):
        brick_file_path = BrickService.pack_brick(brick_directory)
        token = StorageService.get_token()
        params = {
            'token': token
        }

        try:
            files = {'upload': open(brick_file_path, 'rb')}
            url = PATCH_PROJECT_BRICK_URL.replace(':project_id', project_id).replace(':brick_id', brick_id)
            response = requests.patch(url=url, files=files, params=params)

            if response.status_code == requests.codes.ok:
                show_message('Brick successfully updated!')
            elif response.status_code == requests.codes.unauthorized:
                AuthController.logout()
                show_error("Please log in to push brick")
            else:
                show_error("Can't update brick")
        except Exception as e:
            show_error(e)
        finally:
            BrickService.remove_brick_file(brick_file_path)

    @staticmethod
    def delete(brick_directory):
        project_id = StorageService.get_project_id(brick_directory)
        brick_id = StorageService.get_brick_id(brick_directory)
        token = StorageService.get_token()
        params = {
            'token': token
        }

        try:
            url = DELETE_PROJECT_BRICK_URL.replace(':project_id', project_id).replace(':brick_id', brick_id)
            response = requests.delete(url=url, params=params)

            if response.status_code == requests.codes.ok:
                StorageService.delete_brick(brick_directory)
                BrickService.remove_brick_directory(brick_directory)
                show_message('Brick successfully deleted!')
            elif response.status_code == requests.codes.unauthorized:
                AuthController.logout()
                show_error("Please log in to delete brick")
            else:
                show_error("Can't delete brick")
        except Exception as e:
            show_error(e)
