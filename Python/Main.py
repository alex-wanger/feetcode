#!/usr/bin/python3

import cgi
import random


def htmlTop():
    print ('''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <title> Feetcode </title>
        </head>
        <body>''')


def htmlTail():
    print ('''</body>
        </html>''')

def data():
    form = cgi.FieldStorage()
    dic = {}
    for key in form:
        dic[key] = dic.getvalue(key)

def main():
    

if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()
