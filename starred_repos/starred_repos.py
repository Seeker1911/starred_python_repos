import os
import sqlite3
import requests
import datetime
import time
import sys
import json

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
if sys.version_info[0] == 2:
    from api.get_python_stars import get_api, format_json_to_dicts
elif sys.version_info[0] == 3:
    from starred_repos.api.get_python_stars import get_api, format_json_to_dicts


app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , starred_repos.py
# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'starred_repos.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('STARRED_REPOS_SETTINGS', silent=True)


@app.route('/')
def show_entries():
    """Updates DB with most starred Python repos and displays in view. """
    db = get_db()
    cur = db.execute('select distinct name,repo_id,stars, description from python_repos order by stars desc')
    entries = cur.fetchall()
    # get api
    results = get_api()
    # The update operation will consist of deletion and insertion for efficiency
    delete_entry(results)
    add_entry(results)
    return render_template('index.html', entries=entries)


@app.route('/info/<id>')
def info(id):
    """ Shows details of a repo based on repo_id """
    sql = "select distinct name, description, stars, url, last_push_date, repo_id, created_date, avatar from python_repos where repo_id="+id
    db = get_db()
    cursor = db.execute(sql)
    repo_info = cursor.fetchall()
    return render_template('repo.html',info=repo_info)


def delete_entry(results):
    """ Deletes a record before inserting update. """
    repo_ids = [str(item['id']) for item in  results]
    repo_ids = ",".join(repo_ids)
    sql = "DELETE FROM python_repos where repo_id in (:ids)".replace(":ids",repo_ids)
    db = get_db()
    cursor = db.execute(sql)
    db.commit()


@app.route('/add', methods=['POST'])
def add_entry(results):
    """ Insert new repos from API. """
    db = get_db()
    data_to_insert = format_json_to_dicts(results)

    db.executemany("insert into python_repos ( repo_id, name, url, created_date, last_push_date, description, stars, avatar) \
    values (:repo_id, :name, :url, :created_date, :last_push_date, :description, :stars, :avatar)", data_to_insert)

    db.commit()
    flash('Updated ' + str(time.strftime("%Y-%m-%d %H:%M")))
    return redirect(url_for('show_entries'))


# Database helpers
@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
