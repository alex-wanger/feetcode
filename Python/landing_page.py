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
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Python</title>
  <script src="../html/script.js" > </script>
  <link rel="stylesheet" href="../css/basic.css" />
</head>

<body>
  <div id="header-container"></div>

  <main id="main-content">
    
    <p>Welcome to Feetcode {username.value}!</p>

    <section id="history">
     
    </section>
    
    <section id="basics">
     
    </section>

    <section id="libraries">

    </section>

  </main>

  <div id="footer-container"></div>
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
