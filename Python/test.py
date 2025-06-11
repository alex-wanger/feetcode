#!/usr/bin/env python3
import cgi
import csv 
import pandas as pd
from matplotlib import pyplot as plt

def print_html_header():
    print("Content-Type: text/html\n")
    print("""
  <!DOCTYPE html>
<html lang="en">
  
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Ultimate Quiz</title>
  <script src="../html/script.js" > </script>
  <link rel="stylesheet" href="../css/basic.css" />
</head>
<body>
  <div id="header-container"></div>
  <div>
    """)

def print_html_footer():
    print("""
    </div>
    <div id="footer-container"></div>
</body>

</html>
    """)

def printhtml():
    print_html_header()
    #quiz()
    print_html_footer()
def main():
    if __name__ == "__main__":
        try:
            printhtml()
        except:
            cgi.print_exception()

