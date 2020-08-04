'''
Pronic number is a number which is the product of two consecutive integers,
that is, a number n is a product of x and (x+1).
The task is to check and print Pronic Numbers in a range.
Sample input 1:
6
Output:
Pronic Number
Sample input 2:
132
output:
Pronic Number
'''
import math
num=int(input())
i=0
while (i<=int(math.sqrt(num))+1):
    if i*(i+1)==num:
        print('Pronic Number')
        break
    i+=1
else:
    print('Not a Pronic Number')
