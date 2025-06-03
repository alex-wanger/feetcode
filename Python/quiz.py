#!usr/bin/env python3
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

    print()
def get_answer_key(topic):
    file_path = 'output.csv'
    
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

        for row in csv_reader:
            if row[0].strip().lower() == topic.strip().lower():
                return row[1:]
    print(f"data for {topic} not in CSV")

def quiz():
    form = cgi.FieldStorage()
    
    response_data = []
    
    counter = 0

    topic = form.getvalue("quizTopic")
    
    answer_key = get_answer_key(topic)
    
    if len(answer_key) != len(response_data):
        print("Error, please submit all values!")
        return 0

    for i in range(len(answer_key)):
       if answer_key[i] == form.getvalue("r" + str(i)):
           counter += 1
    #change
    values = [(counter/5) * 100, (counter/5) * 100]
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

