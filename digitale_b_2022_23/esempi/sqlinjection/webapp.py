# This example web application is intentionally vulnerable
# to SQL injection; it is meant only as a teaching aid.

import os
import sqlite3


from paste import httpserver  # multithread HTTP server
from bottle import default_app, post, request, route, run, template


def check_login(username, password):
    script_dir = os.path.dirname(__file__)
    con = sqlite3.connect(os.path.join(script_dir, "users.db"))
    cur = con.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    print("QUERY:", query)
    try:
        cur.execute(query)
        rows = cur.fetchall()
    except:
        # If the query is incorrect, return False (login NOT OK)
        return False, query
    if rows:
        login_ok = True
    else:
        login_ok = False
    con.close()
    return login_ok, query


@route("/")
def index():
    return template("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>SQL injection example - Login</title>
        </head>
        <body>
            <div style="width: 300px; margin: auto">
                <h3>Ultra Secure Web App</h3>
                <form action="/login" method="POST">
                    <label for="username">User name:</label><br>
                    <input type="text" id="username" name="username"></label><br><br>
                    <label for="lname">Password:</label><br>
                    <input type="password" id="password" name="password"><br><br>
                    <label for="show"><input type="checkbox" id="show" onchange="toggle_password()">Show password</label><br><br>
                    <input type="submit" value="Login">
                </form>
            </div>
            <script>
                // Simple JavaScript to toggle the password's input content visibility
                function toggle_password() {
                    var password = document.getElementById("password");
                    if (password.type === "password") password.type = "text";
                    else password.type = "password";
                }
            </script>
        </body>
    </html>
    """)


@post("/login")
def login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    login_ok, query = check_login(username, password)
    if login_ok:
        login_message = f"<span style=\"color: green\">Login successful, welcome <strong>{username}</strong>!</span>"
    else:
        login_message = "<span style=\"color: red\">Login failed, try again...</span>"
    return template(f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>SQL injection example - After login</title>
        </head>
        <body>
            <div style="width: 500px; margin: auto">
                <h3>Ultra Secure Web App</h3>
                <p>{login_message}</p>
                <p><a href="/">&larr; Back to login</a></p><br><br>
                <p>
                    SQL query:<br>
                    <pre>{query}</pre>
                </p>
            </div>
        </body>
    </html>
    """)


httpserver.serve(default_app(), host="127.0.0.1", port=8080)