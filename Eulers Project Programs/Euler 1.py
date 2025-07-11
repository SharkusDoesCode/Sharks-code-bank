max = 1000
list = []
for i in range(1, max):
    if i % 3 == 0 or i % 5 == 0:
        list.append(i)
print(sum(list))