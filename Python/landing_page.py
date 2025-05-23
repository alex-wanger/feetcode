#!/usr/bin/env python3

import os
import http.cookies

print("Content-Type: text/html\n")

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
username = cookie.get("username")

def html():
    print(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Welcome</title>
        <link rel="stylesheet" href="../css/styles.css">
        </head>
            <body>
                <div class="navbar">
                        <span style="text-align:left;"><a href="/~awang70/public_html/feetcode/html/landing_page.html">Home</a></span>
                        <a href="/~awang70/feetcode/html/java.html">Java</a>
                        <a href="/~awang70/feetcode/html/python.html">Python</a>
                        <a href="/~awang70/feetcode/html/racket.html">Racket</a>
                        <a href="/~awang70/feetcode/html/quiz.html">Quiz</a>
                </div>
    <div class="container">
        <h1>Welcome, <strong>{username.value}!</strong></h1>
        <p>This is your landing page!</p>
    </div>
</body>
</html>
""")


 


def main():
    html()    

if __name__ == "__main__":
    try:
        main()
    except():
        cgi.print_exception()
