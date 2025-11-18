array = [7, 5, 2, 9, 8]
count = 0
ans = 0

for i in array:
    if i % 2 == 0:
     count= count + 1
     ans = count
print(ans)