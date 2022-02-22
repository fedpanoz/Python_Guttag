sum = 0
for num in range(3, 1000, 2):
    for div in range(3, num, 2):
        if num % div == 0:
            break
    else:
        sum += num
print(sum)

