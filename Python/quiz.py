#!usr/bin/env python3
import cgi
import csv 
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

    print()

def quiz():
    form = cgi.FieldStorage()
    response_data = []
    for i in range(5):
        response_data = form.getvalue("r" + str(i))
    
    
    answer_key = [answer1, answer2, answer3]

    counter = 0
    for i in range(len(data)):
        if data[i] == answer_key[i]:
            counter += 1 
    
    values = [(counter/3) * 100, (counter/3) * 100]
    labels = 'True', 'False'
    print(f"{counter}")
    #plt.pie(values)
def printhtml():
    print_html_header()
    quiz()
    print_html_footer()
def main():
    if __name__ == "__main__":
        try:
            printhtml()
        except:
            cgi.print_exception()

