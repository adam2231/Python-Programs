#Scans a txt file (mbox-short) to find email address, extracts that data and finds the hours that those emails were sent

fname = input('Enter File: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
email = open(fname)

counts = dict()

for line in email:
    if line.startswith("From "):
        time = line.split()[5].split(":")
        counts [time[0]] = counts.get(time[0], 0) + 1

list = list()

for k, v in counts.items():
    list.append( (k, v) )
list.sort()

for hour, counts in list:
    print(hour, counts)
