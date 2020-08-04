'''
Python Program to Check if a Number is a Strong Number
A Strong Number is a number that is equal to the sum of factorial of its digits.
sample input 1:
145
output 1:
Strong Number
Sample input 2:
242
output2:
Not a Strong Number
'''
num=int(input())
temp=num
sum1=0
while num:
    r=num%10
    i=1
    factriol=1
    #print(r)
    while (i<=r):
        factriol=factriol*i
        i+=1
    sum1+=factriol
    num=num//10
if temp==sum1:
    print('Strong Number')
else:
    print('Not a Strong Number')
