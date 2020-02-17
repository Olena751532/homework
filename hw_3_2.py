st = "Hello World"
reversed = ''.join(reversed(st))
print(reversed)

st = "Hello world"
reversedString = []
index = len(st)
while index > 0:
    reversedString += st[index - 1]
    index = index - 1
print(reversedString)

