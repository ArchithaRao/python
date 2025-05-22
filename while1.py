# Q1 : Multiplication Table (1 to 10)
# Write a Python program using nested loops to print the multiplication tables from 1 to 10.
# n=10
# j=1
# while j<=10:
#     i=1
#     while i<=10:
#         print(j,'*',i,'=',j*i)
#         i += 1
#     j += 1


# Q2. Count Prime Numbers in a Range (1 to 100)
# Using nested loops, count how many prime numbers exist between 1 and 100.
# Hint : A number is prime if it’s only divisible by 1 and itself.
# for num in range(2,100):
    
#     for i in range(1,num+1):
#         if num%i==0:
#             print(num)
prime_count=0          
for num in range(2, 100): 
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count == 2:
         prime_count += 1
         print(num)
print("total prime numbers between 1 to 100:",prime_count)         


