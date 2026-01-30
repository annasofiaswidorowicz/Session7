#FOR is more direct - shorter, less explanations
num = 0
while num < 10:
    print(num)
    num = num + 1

for i in range(10):
    print(i)
for i in range(-10, 10, 2): #start, end, steps
    print(i)

#printing the multiplication table
for i in range(1, 11):
    for j in range(i, 11): #start from i so they don't repeat
        print(f"{i} x {j} = {i * j}")
    print()
