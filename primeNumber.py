#--------------------------using for loop---------------------
n=int(input('Enter a number'))
if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            print('not a prime')
            break
    else:
        print('prime')   
else:
    print('not a prime ')    

#---------OR-------
n=int(input('Enter a number'))
if n<=1:
    print('not a prime ')
else:
    for i in range(2,n//2+1):
        if n%i==0:
            print('not a prime')
            break
    else:
        print('prime')    



#------------------------using while loop---------------------
n=int(input('Enter a number'))
i=2
if n>1:
    while i<n//2+1:
        if n%i==0:
            print('not a prime')
            break
        i+=1
    else:
        print('prime')   
else:
    print('not a prime ')  

#-------OR-----
n=int(input('Enter a number'))
i=2
if n<=1:
    print('not a prime')
else:
    while i<n//2+1:
        if n%i==0:
            print('not a prime')
            break
        i+=1
    else:
        print('prime')    


#-------------------------using function-----------------
def checkPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                print('not a prime')
                break
        else:
            print('prime')   
    else:
        print('not a prime ') 
checkPrime(n=int(input('Enter a number')))  

#------OR------
def checkPrime(n):
    i=2
    if n<=1:
        print('not a prime')
    else:
        while i<n//2+1:
            if n%i==0:
                print('not a prime')
                break
            i+=1
        else:
            print('prime')
checkPrime(n=int(input('Enter a number')))