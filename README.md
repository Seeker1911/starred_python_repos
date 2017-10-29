**Most Starred Public Python Repositories**
-----


**Architecture**
---
This project is built on Flask with Python 3 and a SQL Database.
  * It uses the Github api.
  * It uses pip as the package manager.
  * It uses CSS and Bootstrap 3 for styling.
  * It has been tested with with Python versions 2.7 and 3.6.2

**What does it do?**
---
Every time the homepage is loaded it fetches the latest most starred
Python repositories in Github and updates it's local database with new information. That info is then displayed in a timeline view ordered by
most popular at the top. Clicking on a repo will show a more detailed view
of the project including a link to the Github page and the avatar.

**How to run it with virtualenv**
* `$ git clone`
* `$ cd starred_python_repos`
* `$ virtualenv env`
* `$ cd env`
* `$ source bin/activate`
* `$ cd ..`
* `$ pip install -r requirements.txt`
* `$ cd starred_repos`
* `$ export FLASK_APP=starred_repos.py`
* `$ flask run`

**How to run it with conda**
* `$ git clone`
* `$ cd into starred_python_repos`
* `$ conda env create -f environment.yml`
* `$ source activate starred_repos`
* `$ conda list`
* `$ pip install -r requirements.txt`
* `$ cd starred_repos`
* `$ export FLASK_APP=starred_repos.py`
* `$ flask run`

**Useful links**
* virtualenv: https://virtualenv.pypa.io/en/stable/
* anaconda: https://www.anaconda.com
* python.org: https://www.python.org
* Github API: https://developer.github.com/v3/
