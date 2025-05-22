# # Sum of odd numbers from 1 to 10
# sum_of_odds = 0
# num = 1

# while num <= 10:
#     if num % 2 != 0:
#         sum_of_odds += num
#         print(sum_of_odds)
#     num += 1

# #print sum of even numbers from 1 to 10
# sum_of_even = 0
# num = 2

# while num <= 10:
#     if num % 2 == 0:
#         sum_of_even += num
#         print(sum_of_even)
#     num += 1

# #print sum of all numbers
# sum=0
# num=1
# while num<=10:
#         sum +=num
#         print(sum)
#         num += 1
    
# #find the greatest of 2 numbers
# a=3
# b=6
# while a>b:
#     print(a)
# print(b)

# #find the greatest of 3 numbers
# a=6
# b=3
# c=9
# while True:
#     if a>b&a>c:
#         print(a)
#     elif b>c&b>a:
#         print(b)
#     else:
#         print(c)
#         break

# #find whether the year is leap year or not
# year = 2005
# leap_year = False
# i = 0
# while i < 1:
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         leap_year = True
#     i += 1

# if leap_year:
#     print("leap year")
# else:
#     print("not a leap year")

#print tables using loops 
# n=5
# x=1
# while x<=10:
#     print(n,'*',x,'=',n*x)
#     x += 1

# n = 5
# x = 1

# while x <= 10:
#     print(n,'*', x, '=', n * x)
#     x += 1

#Table2
# n=2
# x=1
# while x<=10:
#     print(n,'*',x,'=',n*x)
#     x += 1

#Table3
# n=3
# x=1
# while x<=10:
#     print(n,'*',x,'=',n*x)
#     x += 1

#table4
# n=4
# x=1
# while x<=10:
#     print(n,'*',x,'=',n*x)
#     x += 1    

#table1
# n=1
# x=1
# while x<=10:
#     print(n,'*',x,'=',n*x)
#     x += 1

#patterns
# n=1
# while n<=10:
#     print(str(n)*n)
#     n += 1
        
# n = 5
# x = 1

# while x <= 10:
#     print(n, '*', x, '=', n * x)
#     x += 1

#patterns
# n=1
# while n<=5:
#     print('*'*n)
#     n += 1
   
a=1
for i in range(3):
    a=a**2
    print(a)
