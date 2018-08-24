# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 11:06:09 2018

@author: Tsur
"""
# n is a not negetive interger the function returns the digits of the numer in a reversed order
def reverse_number (n) :
    ans=0
#    [int(my_list) for my_list in str(n)]
#    for i in range(0,len(my_list),2):
#        temp = my_list[i]
#        my_list[i] = my_list[ len( my_list ) - i]
#        my_list[ len( my_list ) - i] = temp
#        ans+=my_list[i]*10**(len(my_list)-1)
#    print ans
#    return ans
    while n >0  :
        ans *= 10
        ans += n % 10
        n = n / 10
    return ans
    
#return the sum of the list
def sum_list (lst):
    sum=0
    for num in lst:
        sum+=num
    return sum

print (sum_list(([1,5,3,1,32])))

def find_strings_with_digit(string_list ,d ):
    