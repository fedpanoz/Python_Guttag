count = 0
for i in range(2, 100):

    for div in range(2, 100):
        if i % div == 0:
            count = count + 1
            break
    if count == 0:
        print(i)