#!/usr/bin/env python3
import cgi
import http.cookies
import os

users_data = "../Python/.users_data.txt"

def print_html_header():
    print("""<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="utf-8">
    <title>Feetcode</title>
    <script src="../html/script.js"></script>
    <link rel="stylesheet" href="../css/basic.css">
</head>
<body>
<div id="header-container"></div>
<main id="main-content">
""")

def print_html_footer():
    print("""
</main>
<div id="footer-container"></div>
</body>
</html>
""")

def print_login_form():
    print("""
    <div class="form-container">
        <h2>Login</h2>
        <form action="../Python/login.py" method="post">
          <label for="userfield">Username or Email</label>
          <input type="text" id="userfield" name="userfield" autocomplete="username" required>

          <label for="password">Password</label>
          <input type="password" id="password" name="password" autocomplete="current-password" required>

          <input type="submit" value="Login" class="submit-button">
        </form>
    </div>
    """)

def main():
    form = cgi.FieldStorage()
    userfield = form.getvalue("userfield")
    password = form.getvalue("password")

    if not userfield or not password:
        print("Content-Type: text/html")
        print() 
        print_html_header()
        print("<div class='status-message error'>Error: Please provide username/email and password.</div>")
        print_login_form()
        print_html_footer()
        return

    data = {}
        with open(users_data, "r") as file:
            for line in file:
                line = line.strip()
                user, pw, email = line.split(":")
                data[user] = (pw, email)
    except FileNotFoundError:
        pass

    valid_user = None
    for user, (pw, email) in data.items():
        if (userfield == user or userfield == email) and password == pw:
            valid_user = user
            break

    if valid_user:
        cookie = http.cookies.SimpleCookie()
        cookie["username"] = valid_user
    
        print("Content-Type: text/html")
        print(cookie.output())
        print()  

        print_html_header()
        print(f'<div class="status-message success">Welcome back, {valid_user}!</div>')
        print("""
        <section>
          <h1>Explore More</h1>
          <p>Be sure to check out our other pages to learn all about Racket, Java, and Python.</p>
          <p>After exploring, take their individual quizzes to test your knowledge.</p>
          <p>And when you're ready, challenge yourself by taking the Ultimate Quiz!</p>
          <p>All of these are easily accessible from our navigation bar at the top.</p>
        </section>
        """)
        print_html_footer()
    else:
        print("Content-Type: text/html")
        print()  
        print_html_header()
        print("<div class='status-message error'>Login failed: Invalid username/email or password.</div>")
        print_login_form()
        print_html_footer()

if __name__ == "__main__":
    try:
        main()
    except Exception:
        cgi.print_exception()
