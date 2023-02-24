# My School

**Project name:** 

**Application name:** AppCoder

**Language:** Python 3.10

**Framework:** Django 4.1

# Structure

The project follows the standard skeleton suggested by Django.

| Directory                            | Description                                                                                    |
|--------------------------------------|------------------------------------------------------------------------------------------------|
| [AppCoder/](AppCoder)                | Contains the code related to the application AppCoder                                          |
| [ProyectoCoder/](ProyectoCoder)      | Contains the general settings of the project.                                                  |
| [static/](static)                    | Contains the static content for Django templates.                                              |
| [templates/](templates)              | Contains the templates to be used by Django views.                                             |
| [db.sqlite3](db.sqlite3)             | SQLite database storing general configurations of the project and </br> Django models and data |
| [manage.py](manage.py)               | Main utility to handle setups and settings of this Django project.                             |
| [requirements.txt](requirements.txt) | Requirements file with the installed libraries for this project.                               |

# Installation

## Virtual environment creation

There are 2 ways to create your virtual environment.
1. From PyCharm, go to File > Settings... > Project:  > Project Interpreter > Add Interpreter...
2. In console, execute the following command:

```console
> python -m venv venv/
```

## Requirements install

Once the virtual environment is read, activate it by executing this command.

```console
> ./venv/Scrtips/activate 
```

*NOTE:* Once there is no need for the virtual environment, execute this command:

```console
(venv) > deactivate 
```

The previous command will activate the virtual environment, which add "(venv)" just to left of the console prompt. 

Now install the requirements in this environment:

```console
(venv) > python -m pip install -r requirements.txt
```
