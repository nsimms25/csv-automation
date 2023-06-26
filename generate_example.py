import pandas as pd
import csv
import random

case_numbers = []
tasks = ["Perform", "Verify"]
performer = ["Nick", "John", "Jane", "Andrew"]

for i in range(0,10):
    case_numbers.append(random.randrange(1234,1212157))

#print(case_numbers)

case_list = []

for case in case_numbers:
    person = random.choice(performer)
    for task in tasks:
        #Choose random person
        assigned_case = (case, task, person)
        case_list.append(assigned_case)

#print(case_list)

df = pd.DataFrame(case_list, columns=['case_number', "task", "performer"])

#print(df)

df.to_csv("example_tasks.csv")
