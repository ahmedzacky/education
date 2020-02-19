handle = open("mbox-short.txt")
sender = {}

for line in handle:
    if line.startswith('From '):
        words = line.split()
        emails = words [1]
        sender[emails] = sender.get(emails, 0) + 1
        
bigsend = None
bigcount = None

for x,y in sender.items():
    if bigcount is None or y > bigcount:
    	bigcount = y
    	bigsend = x
    
print (bigsend, bigcount)