"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

list_of_phone_numbers = []
for i in texts:
    list_of_phone_numbers.append(i[0])
    list_of_phone_numbers.append(i[1])
for i in calls:
    list_of_phone_numbers.append(i[0])
    list_of_phone_numbers.append(i[1])
print("There are", len(set(list_of_phone_numbers)),"different telephone numbers in the records")
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
