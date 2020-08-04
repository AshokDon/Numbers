'''
Spy Number
A number is said to be a Spy number if the sum of all the digits
is equal to the product of all digits.
Sample input 1:
132
Output:
Spy Number
Sample input 2:
1412
output:
Spy Number
'''
num=int(input())
sum_of_digits=0
product_of_digits=1
while num:
    r=num%10
    sum_of_digits+=r
    product_of_digits=product_of_digits*r
    num=num//10
if sum_of_digits==product_of_digits:
    print('Spy Number')
else:
    print('Not Spy Number')
