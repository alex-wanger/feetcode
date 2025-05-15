#!/usr/bin/python3

import cgi, os

def header():
    print("Content-type: text/html\n")
    print("""
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8">
            <title>Feetcode</title>
        </head>
        <body>
    """)

def htmlTail():
    print("""
        </body>
    </html>
    """)

def data():
    form = cgi.FieldStorage()

    username = form.getvalue("username")
    password = form.getvalue("password")

    users_file = "/home/students/odd/2027/awang70/public_html/feetcode/users_data.txt"

    if username and password:
        with open("users_data.txt", "a") as text:
            text.write(f"{username}:{password}\n")
        print("<p>Registered successfully.</p>")
        print("<p><a href='login.html'>Login Now</a></p>")
    else:
        print("<p>Error: Username or password missing.</p>")

def main():
    header()
    data()
    htmlTail()

if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()

