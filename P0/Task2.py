"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

list_of_phone_on_call = []
for i in calls:
    list_of_phone_on_call.append(i[0])
    list_of_phone_on_call.append(i[1])
phone_numbers = set(list_of_phone_on_call)

dict_of_phone_number = {}

for i in phone_numbers:
    dict_of_phone_number[i] = 0

for i in dict_of_phone_number:
    for j in calls:
        if i == j[0] or i == j[1]:
            # print(j[3])
            dict_of_phone_number[i]= dict_of_phone_number[i] + int(j[3]) 
time_spent = []
number = []
for k in dict_of_phone_number:
    time_spent.append(dict_of_phone_number[k])
    number.append(k)

max_index = time_spent.index(max(time_spent))
print(number[max_index], "spent the longest time", max(time_spent), "seconds, on the phone during September 2016")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

