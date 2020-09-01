import requests

from datrics.services.storage_service import StorageService
from datrics.services.show_data_service import ShowDataService
from datrics.services.show_message import show_error, show_message
from datrics.controllers.auth_controller import AuthController
from datrics.constants.links import GET_PROJECTS_URL


class ProjectsController:

    @staticmethod
    def get_projects():
        token = StorageService.get_token()
        params = {
            'token': token
        }
        response = requests.get(url=GET_PROJECTS_URL, params=params)

        if response.status_code == requests.codes.ok:
            projects = response.json()
            ShowDataService.show_projects(projects)
        elif response.status_code == requests.codes.unauthorized:
            AuthController().logout()
            show_error("Please log in to get projects")
