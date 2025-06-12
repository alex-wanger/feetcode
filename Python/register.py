#!/usr/bin/python3

import cgi
import http.cookies
import os

users_data = "../Python/.users_data.txt"

def print_html_header():
    print("Content-type: text/html\n")
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

def print_register_form():
    print("""
    <div class="form-container">
      <h2>Register</h2>
      <form action="../Python/register.py" method="post">
        <label for="username">Username</label>
        <input type="text" name="username" required>

        <label for="email">Email</label>
        <input type="email" name="email" required>

        <label for="password">Password</label>
        <input type="password" name="password" required>

        <input type="submit" value="Register" class="submit-button">
      </form>
    </div>
    """)

def main():
    form = cgi.FieldStorage()
    username = form.getvalue("username")
    password = form.getvalue("password")
    email = form.getvalue("email")
    data = {}
    try:
        with open(users_data, "r") as file:
            for line in file:
                user, pw, em = line.strip().split(":")
                data[user] = (pw, em)
    except FileNotFoundError:
        pass  

    print_html_header()

    if not username or not password or not email:
        print('<div class="smessage error">Missing fields. Please go back and try again.</div>')
        print_register_form()
        print_html_footer()
        return

   
    if username in data:
        print('<div class="smessage error">Username taken. Try with a new one.</div>')
        print_register_form()
        print_html_footer()
        return
    try:
        with open(users_data, "a") as f:
            f.write(f"{username}:{password}:{email}\n")
    except Exception as e:
        print(f'<div class="smessage error">Error saving data: {e}</div>')
        print_register_form()
        print_html_footer()
        return

    cookie = http.cookies.SimpleCookie()
    cookie["username"] = username
    

    print(f'<div class="smessage success">Welcome, {username}! You have been registered and automatically logged in.</div>')
    print("""
    <section>
      <h1>Explore More</h1>
      <p>Be sure to check out our other pages to learn all about Racket, Java, and Python!</p>
      <p>After exploring, take their individual quizzes to test your knowledge.</p>
      <p>And when you’re ready, challenge yourself by taking the Ultimate Quiz!</p>
      <p>All of these are easily accessible from our navigation bar at the top.</p>
    </section>
    """)
    print_html_footer()

if __name__ == "__main__":
    try:
        main()
    except Exception:
        import cgi
        cgi.print_exception()
