# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""   

arr = []
def push():
    a = int(input("Enter data : "))
    arr.append(a)
    
def display():
    print(arr)
        
def ins_pos():
    pos = int(input("Enter position : "))
    a = int(input("Enter data : "))
    arr.insert(pos, a)
    display()

def delete():
    del(arr[0])
    display()
    
def del_pos():
    pos = int(input("Enter the possition to delete elements : "))
    del(arr[pos])
    display()

while(1):
    print("1. push : \n2. insert specific position : \n3. delete : \n4. delete position wise : ")
    ch = int(input("Enter your choice : "))
    if(ch == 1):
        push()  
        display()
    elif(ch == 2):
        ins_pos()
    elif(ch == 3):
        delete()
    elif(ch == 4):
        del_pos()
    else:
        print("invalid");
        
    
