handle = open('mbox-short.txt')

dick = {}
myList = []

for line in handle:
    if line.startswith('From '):
        line = line.split()
        time = line[5]
        time = time.split(':')
        hour = time[0]
        dick[hour] = dick.get(hour,0) + 1

for x,y in dick.items():
    myList.append((x,y))

myList.sort()

for x,y in myList:
    print (x, y)
   