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

def part3():
    my_list = [1, 7, 9, 15, 2, 8]
# begin your code here
 
def even (x):
#inpout= number 
#output= true if the number is even and false if not 
    if x%2==0 :
        return  True
    else:
        return False
  
 
 
    my_list = [1, 7, 9, 15, 2, 8]
    even_list = [my_list[x] for x in range (len(my_list)) if even(my_list[x]) ]
    odd_list = [my_list[x] for x in range (len(my_list)) if not even(my_list[x]) ]
    print even_list
    print odd_list


def part4():
    sum=0
    my_list = [[1,3,5],[3,2],[], [-17]]
    for i in range(len(my_list)) :
        for j in range (len(my_list[i])) :
            if ( i % 2 == 0 ):
                if(j % 2 == 0 ):
                    sum += my_list[i][j]
            else:
                if(j % 2 == 1):
                    sum +=my_list[i][j]
                   
    print sum


def part5():
    mystring1 = raw_input('Please enter a string: ')
    mylist1 = list(mystring1.split())
    mystring2 = raw_input('Please enter a string: ')
    mylist2 = list(mystring2.split())
    print 'true' if mylist1 == mylist2 else 'false'

part5()










    