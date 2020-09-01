import click

from datrics.controllers.auth_controller import AuthController
from datrics.controllers.projects_controller import ProjectsController
from datrics.controllers.brick_controller import BrickController
from datrics.services.brick_service import BrickService
from datrics.services.storage_service import StorageService
from datrics.constants.links import PROD_BASE_API_URL


@click.group(chain=True)
@click.version_option("0.0.1")
def main():
    """Create and update custom bricks in Datrics CLI mode"""

"""
Init Command
"""
@click.command(
    help='Init custom bricks repository'
)
def init():
    BrickService.init_bricks_repository()


"""
Auth Commands
"""
@click.command(
    help='Authenticate user on Datrics platform'
)
@click.option(
    '-e', '--email',
    prompt=True,
    required=True,
    help='user email on the Datrics account',
)
@click.option(
    '-p', '--password',
    hide_input=True,
    prompt=True,
    required=True,
    help='user password on the Datrics account',
)
def login(email, password):
    AuthController.login(email, password)


@click.command(
    help='Logout user from Datrics platform'
)
def logout():
    AuthController.logout()


"""
create Command
"""
@click.command(
    help='Create custom brick template'
)
@click.option(
    '-p', '--project-id',
    prompt=True,
    required=True,
    help='project id on the Datrics account',
)
@click.option(
    '-b', '--brick-directory-name',
    prompt=True,
    required=True,
    
    help='prompt brick directory name',
)
@click.option(
    '-b', '--brick-name',
    prompt=True,
    required=True,
    help='prompt brick name',
)
def create(project_id, brick_directory_name, brick_name):
    BrickService.create_template_brick(project_id, brick_directory_name, brick_name)


"""
Push Command
"""
@click.command(
    help='Add brick to the project on Datrics platform'
)
@click.option(
    '-b', '--brick-directory-name',
    prompt=True,
    required=True,
    help='prompt brick directory name',
)
def push(brick_directory_name):
    BrickController.push(brick_directory_name)


"""
Rm Command
"""
@click.command(
    help='Add brick to the project on Datrics platform'
)
@click.option(
    '-b', '--brick-directory-name',
    prompt=True,
    required=True,
    help='prompt brick directory name',
)
def rm(brick_directory_name):
    BrickController.delete(brick_directory_name)


"""
Projects Command
"""
@click.command(
    help='Get projects (id and name) from Datrics platform'
)
def projects():
    ProjectsController.get_projects()


"""
Env Command
"""
@click.command(
    help=f'Change base api url from `{PROD_BASE_API_URL}` to another url'
)
@click.option(
    '-u', '--url',
    prompt=True,
    required=True,
    help='prompt url to api',
)
def env(url):
    StorageService.save_api_base_url(url)


"""
Add commands to CLI
"""
main.add_command(init)
main.add_command(login)
main.add_command(logout)
main.add_command(create)
main.add_command(push)
main.add_command(rm)
main.add_command(projects)
main.add_command(env)


if __name__ == '__main__':
    main()
