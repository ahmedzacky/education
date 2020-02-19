text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')

x = text[pos+1:]
y = float(x)
print(y)