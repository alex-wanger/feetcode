#!/usr/bin/env python3

import os
import http.cookies

print("Content-Type: text/html\n")

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
username = cookie.get("username")


def navbar():
    print("""<div class="navbar">
        <a href="/~awang70/feetcode/html/java.html">Java</a>
        <a href="/~awang70/feetcode/html/python.html">Python</a>
        <a href="/~awang70/feetcode/html/javascript.html">JavaScript</a>
        <a href="/~awang70/feetcode/html/github.html">Git</a>
    </div>
        """)
def header():
    print("<!DOCTYPE html>")
    print("<html lang='en'>")
    print("<head>")
    print("<link rel='stylesheet' href='/~awang70/feetcode/css/styles.css'>")
    print("<title>Landing Page</title>")
    print("</head>")
    print("<body>")
    navbar() 
    print("<h1>Welcome to Feetcode!</h1>")


def welcome():
    if username:
        print(f"<p>Hello, <strong>{username.value}</strong></p>")
    else: 
        print("<p> Error </p>")

def footer():
    print("</body></html>")


def main():
    header()
    welcome()
    footer()

if __name__ == "__main__":
    try:
        main()
    except():
        cgi.print_exception()
