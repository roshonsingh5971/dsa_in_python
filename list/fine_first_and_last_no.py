# numbers = [10, 20, 30, 40, 50]

# first = numbers[0]
# last = numbers[-5]

# print(first, last)

numbers = [10, 20, 30, 40, 50]

# numbers ka lenght 
n = len(numbers)

#fine  fist number 

first =None

# fine the last number
last = None

for idx in range(n):
    if idx == 0 :
        first = numbers[idx]

    if idx == n-1 :
        last = numbers[idx]


print (first , last)



