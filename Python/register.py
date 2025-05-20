#!/usr/bin/python3

import cgi

users_data = "/home/students/odd/2027/awang70/public_html/feetcode/.users_data.txt"

def redirect_to_login():
    print("Status: 302 Found")
    print("Location: /~awang70/feetcode/html/login.html")
    print()  

def print_html_header():
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

def print_html_footer():
    print("""
        </body>
    </html>
    """)

def main():
    form = cgi.FieldStorage()
    username = form.getvalue("username")
    password = form.getvalue("password")
    email = form.getvalue("email")
    key_values = {}
    with open(users_data, "r") as file:
        for line in file:
             line = line.rstrip("\n")
             key, value = line.split(":")
             key_values[key] = value

    if username in key_values:
        print_html_header()
        print("<p>Username taken, try with a new username.</p>")
        print_html_footer()
    
    elif username and password and username not in key_values:
        try:
            with open(users_data, "a") as f:
                f.write(f"{username}:{password}\n")
            redirect_to_login()
        except Exception as e:
            print_html_header()
            print(f"<p>Error saving data: {e}</p>")
            print_html_footer()
    else:
        print_html_header()
        print("<p>Error: Username or password missing.</p>")
        print_html_footer()

if __name__ == "__main__":
    try:
        main()
    except Exception:
        import cgi
        cgi.print_exception()

