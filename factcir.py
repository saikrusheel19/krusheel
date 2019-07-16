num = int(input())
fact = 1
if(num%2 == 0):
    num1 = num-1
    for i in range(1,num1+1): 
        fact = fact * i 
    print (fact)
else:
    print('invalid')
