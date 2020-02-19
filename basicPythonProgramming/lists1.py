fname = input("Please enter file name: ")
try:
    fhand = open(fname)
except:
    print(f'file "{fname}" not found')
    quit()
myList = []

for line in fhand:
    words = line.split()
    for word in words:
        if word in myList:
            continue
        myList.append(word)

myList.sort()
print(myList)