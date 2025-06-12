#!/usr/bin/env python3
import cgi
import csv
import matplotlib.pyplot as plt


def print_html_header():
    print("Content-Type: text/html\n")
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <title>Ultimate Quiz</title>
      <script src="../html/script.js"></script>
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

    response_data = []
    for i in range(len(answer_key)):
        answer = form.getvalue("q" + str(i+1))
        response_data.append(answer)

    counter = sum(1 for i in range(len(answer_key)) if answer_key[i] == response_data[i])
    
    
    
    print(f"<h2>Quiz Language: {topic}</h2>")
    print(f"<p>You got {counter} out of {len(answer_key)} correct.</p>")
    
    labels = ['Correct', 'Incorrect']
    sizes = [counter, len(answer_key) - counter]
    colors = ['Blue', 'Red']

    plt.figure(figsize=(4, 4))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.axis('equal') 

    
    chart_path = "/home/students/odd/2027/awang70/public_html/feetcode/images/quiz_result.png"
    plt.savefig(chart_path)
    plt.close()

    print('<img src="/~awang70/feetcode/images/quiz_result.png" alt="Quiz Result Chart" width="300"/>')




    

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
