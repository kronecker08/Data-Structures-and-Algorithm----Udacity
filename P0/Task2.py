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


dict_of_phone_number = dict()

for i in calls:
    if i[0] in dict_of_phone_number:
        dict_of_phone_number[i[0]] += int(i[3])
    else:
        dict_of_phone_number[i[0]] = int(i[3])
    if i[1] in dict_of_phone_number:
        dict_of_phone_number[i[1]] += int(i[3])
    else:
        dict_of_phone_number[i[1]] = int(i[3])

num_long_time = max(dict_of_phone_number, key= dict_of_phone_number.get)
long_time = dict_of_phone_number[num_long_time]
print("{} spent the longest time {} seconds, on the phone in September 2016".format(num_long_time, long_time))


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

