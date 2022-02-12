# Python program to display all the prime numbers within an interval

#lower = 2
#upper = 101
#print("Prime numbers between", lower, "and", upper, "are:")

for num in range(2, 101):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)