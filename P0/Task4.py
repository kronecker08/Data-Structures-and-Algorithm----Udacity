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


call_outgoing = []
call_incoming = []


for i in calls:
    call_outgoing.append(i[0])
    call_incoming.append(i[1])
call_outgoing = set(call_outgoing)
call_incoming = set(call_incoming)


num_texts = []
for i in texts:
    num_texts.append(i[0])
    num_texts.append(i[1])

num_texts = set(num_texts)


telemarketers = []
for i in call_outgoing:
    if i in call_incoming:
        continue
    elif i in num_texts:
        continue
    else:
        telemarketers.append(i)

telemarketers = sorted(telemarketers)

print("These numbers could be telemarketers: ")
for i in telemarketers:
    print(i)



"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

