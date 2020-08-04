'''Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
Given a number n the task is to find n is Ugly number.'''
'''
Sample input 1:
6
Output:
Ugly Number
'''
num=int(input())
if num<1:
    print('Not Ugly Number')
else:
    z=[2,3,5]
    for i in z:
        while num%i==0:
            num=num/i
            #print(i,num)
    if num==1:
        print("Ugly Number")
    else:
        print("Not Ugly Number")
