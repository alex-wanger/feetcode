#!/usr/bin/env python3
import cgi
import csv 
from matplotlib import pyplot as plt
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
 

def quiz():
    form = cgi.FieldStorage()
    response1 = form.getvalue("r1")
    response2 = form.getvalue("r2")
    response3 = form.getvalue("r3")
    data = [response1, response2, response3]

    answer1 = "True"
    answer2 = "True"
    answer3 = "True"
    answer_key = [answer1, answer2, answer3]

    counter = 0
    for i in range(len(data)):
        if data[i] == answer_key[i]:
            counter += 1 
    
    labels = []
    values = [(counter/3) * 100, (3 - counter)/3 * 100]
    #make it so that there arent two labels if you get 100 on either true or false
    if values[0] == 100:
        labels.append("True")
        values.pop(1)
    elif values[1] == 100:
        labels.append("False")
        values.pop(0)
    else: 
        labels.append("True"), labels.append("False")


    plt.pie(values, labels=labels, autopct='%.1f%%')
    plt.savefig("mygraph.png")
    print('''<img src="mygraph.png" graph="alt" height="600"> ''')

def printhtml():
    print_html_header()
    quiz()
    print_html_footer()
def main():
    try:
        printhtml()
    except:
        cgi.print_exception()

if __name__ == "__main__":
    main()

