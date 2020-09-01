## Installation
pip install datrics

## Usage

### CLI help
It will show all existing commands:

  datrics --help

### Create custom bricks repository
It will initialize folder with datrics configuration file:
  
  datrics init


### Setup the connection to datrics environment
By default datrics-cli is connected to datrics SaaS environment, 
but if you need to connect to your custom environment or to any
predefined envs you can run this command and pass url of 
your environment.

  datrics env


### Login to Datrics user account
To login to you user account and make it possible to 
load projects or to push bricks you should run:

  datrics login

### Logout on Datrics user account

  datrics logout

### Initialize brick boilerplate
To bootstrap the creation of your custom brick run the next command.
CLI will create folders and files structure for you

  datrics create

### Push (create or update) brick on Datrics user account
It will push the changes that you've made in the code to the platform

  datrics push

### List of projects on your Datrics user account
  
  datrics projects
