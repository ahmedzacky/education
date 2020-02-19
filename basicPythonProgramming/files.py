fname = input('Please enter file name: ')
count = 0
total = 0

try:
    fhand = open(fname)
except:
    print (fname, 'not found')
    quit()

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        x = line.find(':')
        z = float(line[x+1:])
        total = z + total
answer = total / count
print("Average spam confidence:", answer)
