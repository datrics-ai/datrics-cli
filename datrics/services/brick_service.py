import sys, os
import pathlib
import tarfile
import shutil
from cookiecutter.main import cookiecutter

from datrics.services.storage_service import StorageService
from datrics.constants.pathes import TEMPLATE_STORAGE_PATH


class BrickService:

    @staticmethod
    def init_bricks_repository():
        StorageService.create_storage()

    @staticmethod
    def create_template_brick(project_id, brick_directory_name, brick_name):
        file_dir_path = pathlib.Path(__file__).parent.absolute()
        current_dir_path = pathlib.Path().absolute()
        cookiecutter(
            f'{file_dir_path}/{TEMPLATE_STORAGE_PATH}',
            no_input=True,
            output_dir=f'{current_dir_path}',
            extra_context={
                'brick_directory_name': brick_directory_name,
                'brick_name': brick_name,
            }
        )
        StorageService.save_project_id(brick_directory_name, project_id)
    
    @staticmethod
    def pack_brick(brick_directory_name):
        current_dir_path = pathlib.Path().absolute()
        brick_dir_path = f'{current_dir_path}/{brick_directory_name}/'
        brick_file_path = f'{current_dir_path}/{brick_directory_name}.tar'
        try:
            with tarfile.open(brick_file_path, "w") as tar:
                for _, _, filenames in os.walk(brick_dir_path):
                    for filename in filenames:
                        if '.pyc' not in filename:
                            tar.add(brick_dir_path + filename, arcname=filename)
        except Exception as e:
            print(e)
            os.remove(brick_file_path)
            sys.exit(0)
        return brick_file_path

    @staticmethod
    def remove_brick_file(brick_file_path):
        os.remove(brick_file_path)

    @staticmethod
    def remove_brick_directory(brick_directory_name):
        current_dir_path = pathlib.Path().absolute()
        brick_dir_path = f'{current_dir_path}/{brick_directory_name}/'
        shutil.rmtree(brick_dir_path)