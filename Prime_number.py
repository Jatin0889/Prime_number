# 1. WAP to find the prime number  1 to 30 by while loop

number = 1 
while (number <= 30):
    count = 0 
    r = 1 
    while (r <= number):
        if (number % r == 0):
            count = count + 1
        r = r + 1
    if (count == 2 ):
        print("prime",number)
    else:
        print("not prime",number)
    number = number + 1


# 2. WAP to find the prime number  1 to 30 by for loop
for number in range (1,31,1):
    count = 0 
    for i in range(1,number + 1 ,1):
        if (number %i==0):
            count=count+1
    if(count==2):
        print("prime number", number)
    else:
        print("not a prime number",number)


# 3. WAP to find the prime number entered by user through while loop

num = int(input("enter number:"))
factorcount = 0
i = 1
while(i<=num):
    if ( num % i == 0):
        factorcount  = factorcount + 1
    i = i + 1
if(factorcount == 2 ):
    print("it is a prime number")
else:
    print("it is not  a prime number")


# 4. WAP to find the prime number entered by user through for loop 

num=int(input("enter number:"))
factorcount = 0
for i in range(1,num+1,1):
    if(num % i == 0 ):
        factorcount = factorcount + 1
if(factorcount == 2 ):
    print("it is a prime number")
else:
    print("it is not  a prime number")





