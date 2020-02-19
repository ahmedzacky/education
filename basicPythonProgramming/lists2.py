fhand = open('mbox-short.txt')
myList = []
count = 0

for line in fhand:
   line.rstrip()
   if line.startswith('From '):
      words = line.split()
      print (words[1])
      count += 1

print (f'There were {count} line in the file with from as the first word')
