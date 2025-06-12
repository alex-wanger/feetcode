import csv
import numpy as np

file_path = 'output.csv'



def initalize():
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        data = np.array([['quizTopic', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']])
        csv_writer.writerows(data)

    print(f"Data written to {file_path}")
   

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
    print("data succesfully written")  
  
initalize()
addData(['Java', 'A', "B", "C","D","A", "B", "B"]) 