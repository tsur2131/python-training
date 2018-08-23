# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:25:32 2018

@author: Tsur
"""
#part 1 will be a function that recieves a string as an input and 
#prints both the input string and an augumented string that every occorence of 'e' or 'E'
#was changed to 'o' or 'O' accordingly
def part1():
    mystring = raw_input('Please enter a string: ')
    mylist=list(mystring)
    for i in range(len(mystring)):
        mylist[i] = 'o' if mylist[i]=='e' else mylist[i]
        mylist[i] = 'O' if mylist[i]=='E' else mylist[i]
        out=''.join(mylist) 
        print out ,"\n", mystring

#part 2 function received a string conatining an even number of words 
#seperated by space and creates a new string which has the order of the odd
#words changed with the even ones

def part2():
    mystring = raw_input('Please enter a string: ')
    mylist = mystring.split()
    for i in range(0,len(mystring.split()),2) :
        temp=mylist[i]
        mylist[i]=' ' +mylist[i+1] if i!=0 else mylist[i+1]
        mylist[i+1]=' ' + temp
    endstring=''.join(mylist)
    print mystring , "\n", endstring

part2()