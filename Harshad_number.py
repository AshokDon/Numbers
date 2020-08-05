'''
Harshad Number.
If a number is divisible by the sum of its digits, then it will be known as
a Harshad Number.
For example:
The number 156 is divisible by the sum (12) of its digits (1, 5, 6 ).
some of harshad numbers:-->10,12,18,20,120,140,152,156,198,200
'''

num=int(input())
sum_of_digits=0
temp=num
while num:
    r=num%10
    sum_of_digits+=r
    num=num//10
if temp%sum_of_digits==0:
    print('Harshad Number')
else:
    print('Not a Harshad Number')
