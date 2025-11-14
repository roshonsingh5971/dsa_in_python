data = [5 ,2, 10, 9, 13, 0]
x = data
x.append(-1)
minval = data[0]

for i in data:
     if i < minval:
          minval = i
print(minval)
print(x)