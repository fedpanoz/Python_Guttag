summa = 0
for num in range(3, 1000):
    for div in range(2, num):
        if num % div == 0:
            break
    else:
        print(num, end=" ")
        summa += num
print("\n\n", summa)
