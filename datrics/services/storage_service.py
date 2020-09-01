import pathlib
import os, sys
import json

from datrics.constants.pathes import DATRICS_STORAGE_PATH


DATRICS_DEFAULT_STORE = {
    'token': '',
    'bricks': {}
}

class StorageService:

    @staticmethod
    def create_storage():
        store_file = StorageService.get_storage_file()
        if not store_file or len(store_file) == 0:
            StorageService.save_storage()

    @staticmethod
    def save_token(access_token=''):
        try:
            store = StorageService.get_storage()
            store['token'] = access_token
            StorageService.save_storage(store)
        except Exception as e:
            print(e)
            sys.exit(0)

    @staticmethod
    def get_token():
        try:
            store = StorageService.get_storage()
            return store['token']
        except Exception as e:
            print(e)
            sys.exit(0)

    @staticmethod
    def remove_token():
        StorageService.save_token()

    @staticmethod
    def save_brick_id(brick_directory, brick_id=''):
        try:
            store = StorageService.get_storage()
            if not store['bricks'].get(brick_directory):
                store['bricks'][brick_directory] = {
                    'project_id': None,
                    'brick_id': None,
                }
            store['bricks'][brick_directory]['brick_id'] = brick_id
            StorageService.save_storage(store)
        except Exception as e:
            print(e)
            sys.exit(0)

    @staticmethod
    def get_brick_id(brick_directory):
        try:
            store = StorageService.get_storage()
            if not store['bricks'].get(brick_directory):
                raise Exception(f'Brick {brick_directory} does not exists')
            return store['bricks'].get(brick_directory, {}).get('brick_id', None)
        except Exception as e:
            print(e)
            sys.exit(0)

    @staticmethod
    def save_project_id(brick_directory, project_id=''):
        try:
            store = StorageService.get_storage()
            if not store['bricks'].get(brick_directory):
                store['bricks'][brick_directory] = {
                    'project_id': None,
                    'brick_id': None,
                }
            store['bricks'][brick_directory]['project_id'] = project_id
            StorageService.save_storage(store)
        except Exception as e:
            print(e)
            sys.exit(0)

    @staticmethod
    def get_project_id(brick_directory):
        try:
            store = StorageService.get_storage()
            if not store['bricks'].get(brick_directory):
                raise Exception(f'Brick {brick_directory} does not exists')
            return store['bricks'].get(brick_directory, {}).get('project_id', None)
        except Exception as e:
            print(e)
            sys.exit(0)
    
    @staticmethod
    def delete_brick(brick_directory):
        try:
            store = StorageService.get_storage()
            if store['bricks'].get(brick_directory):
                store['bricks'][brick_directory] = None
            StorageService.save_storage(store)
        except Exception as e:
            print(e)
            sys.exit(0)
    
    @staticmethod
    def save_api_base_url(api_base_url=''):
        try:
            store = StorageService.get_storage()
            store['env'] = api_base_url
            StorageService.save_storage(store)
        except Exception as e:
            print(e)
            sys.exit(0)

    @staticmethod
    def get_api_base_url(api_base_url=''):
        try:
            store_file = StorageService.get_storage_file()
            if not store_file or len(store_file) == 0:
                return ''
            store = StorageService.get_storage()
            return store.get('env', '')
        except Exception as e:
            print(e)
            sys.exit(0)

    @staticmethod
    def save_storage(store=DATRICS_DEFAULT_STORE):
        try:
            storage_path = StorageService.get_storage_path()
            store_file = open(storage_path, 'w+')
            store_file.write(json.dumps(store))
            store_file.close()
        except Exception as e:
            print(e)
            sys.exit(0)

    @staticmethod
    def get_storage():
        try:
            store_file = StorageService.get_storage_file()
            if len(store_file) == 0:
                raise Exception('Project is not initialized, please execute `datrics init` to continue')
            else:
                return json.loads(store_file)
        except Exception as e:
            print(e)
            sys.exit(0)

    @staticmethod
    def get_storage_file():
        storage_path = StorageService.get_storage_path()
        mode = 'r+' if os.path.exists(storage_path) else 'w+'
        store_file = open(storage_path, mode)
        store = store_file.read()
        store_file.close()
        return store

    @staticmethod
    def get_storage_path():
        return f'{StorageService.get_current_dir_path()}/{DATRICS_STORAGE_PATH}'

    @staticmethod
    def get_current_dir_path():
        return pathlib.Path().absolute()

