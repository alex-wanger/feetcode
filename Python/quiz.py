#!/usr/bin/env python3
import cgi
import csv
import matplotlib.pyplot as plt
import numpy as np

file_path = "data.csv"

def print_html_header():
    print("Content-Type: text/html\n")
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <title>Quiz Results</title>
      <script src="../html/script.js"></script>
      <link rel="stylesheet" href="../css/basic.css" />
    </head>
    <body>
      <div id="header-container"></div>
      <main id="main-content">
        <section id="chart">
      <div>
    """)

def print_html_footer():
    print("""
      </div>
      </section>
      </main>
      <div id="footer-container"></div>
    </body>
    </html>
    """)

def addData(list1):
    data = []
    with open(file_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        if len(list1) != 8:
            print(f"Error, list length {len(list1)} is incorrect")
            return None

        for i in range(len(list1)):
            data.append(list1[i])
        csv_writer.writerow(data)


def get_answer_key(topic):
    file_path = '../output.csv'
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader) 
        for row in reader:
            if row[0].strip().lower() == topic.strip().lower():
                return row[1:] #return everything BESIDES the topic name 
    print(f"<p>Error: data for {topic} not in CSV</p>")
    return None

def quiz():
    form = cgi.FieldStorage()
    topic = form.getvalue("quizTopic")
    if not topic:
        print(f"<p>Error: {topic} quizTopic not provided.</p>")
        return

    answer_key = get_answer_key(topic)
    if not answer_key:
        return


    addData([form.getvalue("quizTopic"),form.getvalue("q1"),form.getvalue("q2"),form.getvalue("q3"),
              form.getvalue("q4"),form.getvalue("q5"),form.getvalue("q6"),
              form.getvalue("q7")])

    response_data = []

    for i in range(len(answer_key)):
        answer = form.getvalue("q" + str(i+1))
        response_data.append(answer)

    counter = sum(1 for i in range(len(answer_key)) if answer_key[i] == response_data[i])
    
    
    
    print(f"<h1>{topic} Quiz</h1>")
    print(f"<p>You got {counter} out of {len(answer_key)} questions correct.</p>")
    
    labels = ['Correct', 'Incorrect']
    sizes = [counter, len(answer_key) - counter]
    colors = ['Blue', 'Red']

    plt.figure(figsize=(4, 4))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.axis('equal') 

    
    chart_path = "../images/quiz_result.png"
    plt.savefig(chart_path)
    plt.close()

    print('<img src="../images/quiz_result.png" alt="Quiz Result Chart"/>')




    

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


