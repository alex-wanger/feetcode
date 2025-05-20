#!/usr/bin/env python3
import cgi
import http.cookies
user_data = "/home/students/odd/2027/awang70/public_html/feetcode/.users_data.txt"

def print_html_header():
    print("Content-Type: text/html\n")
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Feetcode</title>
    </head>
    <body>
        <h1>Feetcode</h1>
    """)

def print_html_footer():
    print("""
    </body>
    </html>
    """)

    print()

def login():
    form = cgi.FieldStorage()
    username = form.getvalue("username")
    password = form.getvalue("password")

    if not username or not password:
        print_html_header()
        print("<p>Error: Please provide username and password.</p>")
        print_html_footer()
        return

    key_values = {}
    with open(user_data, "r") as file:
        for line in file:
            line = line.strip()
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()
                key_values[key] = value

    if username in key_values and key_values[username] == password:
        print(f"Set-Cookie: username={username}; Path=/")
        print("Status: 302 Found")
        print("Location: /~awang70/feetcode/Python/landing_page.py\n")
    else:
        print_html_header()
        print("<p>Login failed: Invalid username or password.</p>")
        print_html_footer()

def main():
    login()

if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()

