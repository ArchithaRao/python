#print sum of odd numbers from 1 to 10 
sum_of_numbers=0
for i in range (1,11):
    if i%2 != 0:
        sum_of_numbers += i
        print(sum_of_numbers)

#print sum of even numbers 1 to 10
sum_of_numbers=0
for i in range(1,11):
    if i%2 ==0:
        sum_of_numbers=sum_of_numbers+i
        print(sum_of_numbers)

#print sum of all numbers from 1 to 10
sum =0
for i in range(1,11):
     sum=sum+i
     print(sum)
    
#find the greastest of two numbers
n1=5
n2=7
if(n1>n2):
     print(n1)
else:
     print(n2)

#find the greastest of three numbers
a=7
b=15
c=10
if(a>b & a>c):
     print(a)
elif(b>c):
     print(b)  
else:
     print(c)  


#print prime numbers  from 1 to 10
for num in range(2, 11):  # Start from 2 because 1 is not prime
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count == 2:
         print(num)

#find whether the year is leap year or not
num=2025
if(num%4==0):
     print("leap year")
else:
     print("not a leap year")
      


          
