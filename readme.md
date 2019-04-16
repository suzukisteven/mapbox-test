# Scaffold Template

## *** Please clone this repository and do not directly make changes to it ***
### This is our boilerplate code for all apps we produce.
### It helps speed up development time and allow us to spend time focusing on the custom business logic.

<hr>

A few steps are needed before the boilerplate functions properly.

## app.py: Change both to project name

```PYTHON
# Change 'web' to project name.
web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'web')

# Change 'PROJECT' to project name.
app = Flask('PROJECT', root_path=web_dir)
```
<br>
<hr>

## .env: Configure DATABASE_URL

```PYTHON
DATABASE_URL="postgres://localhost:5432/postgres_server_name" # Change to your DB Name
```

###  Then add .env to .gitignore file (not added by default)

<br>
<hr>

## pip install -r requirements.txt
This installs all commonly used Flask dependencies such as peewee, peeweedb-evolve, psycopg2-binary, Flask, Jinja2, Flask-login etc. </br></br> For a complete list of all packages installed check the requirements.txt file.


<br>
<hr>

## server.py: change import name to match project-name folder. i.e. nextagram_web

```PYTHON
import web #<---
```

<br>
<hr>

## Create a PostgreSQL database.

In Terminal:
```PYTHON
createdb project_name_dev
```

<br>
<hr>

## Create a virtual environment (always be in your virtualenv):

In terminal:
```PYTHON
conda create -n project_name python=3.7
conda activate project_name
```

<br>
<hr>

## instead of typing python migrate.py everytime, run this command to type only 'migrate' in terminal to run it:

```PYTHON
echo -e '\nalias migrate="python migrate.py"\n' >> ~/.bash_profile
```

<br>
<hr>

## Build something cool!
```PYTHON
flask run
```
 
