# Romans Kucerenko 4.grupa 211RDB275
import sys
import threading
import numpy as nup

"""
 def node1(n,parent,d):
    if(parent[n]=1):return false
    if(d[n]!=0):return d
    return parent[n]*/ 
"""

def compute_height(n, parents):
    # Write this function
    i,max_height = int(0)
    # Your code her
    part=nup.zeros(n,dtype=int)
    while(i<n):
        part[i]=node2(i,parents,part)     
        i=1+i  
    max_height=nup.amax(part)
    return max_height

def node2(n,parents,d):
    if(parents[n]==-1):return 1
    if(d[n]!=0):return d[n]
    d[n]=node2(parents[n],parents,d)+1
    return d[n]

def main():
    # implement input form keyboard and from files
    Text1=input()
    Text2=input()
    if(Text1.startswith("F")):
        filename="test/"+Text2
        if(filename.endswith("a")):return
        file=open(filename,"r")
        n=int(file.readline())
        Text1=(file.readline())
        first=Text1.split()
        arr=nup.asarray(first,dtype=int)
        g=compute_height(n,arr)
        print(g)
    elif(Text1.startswith("I")):
        n=int(Text2)
        Text3=input()
        first=Text3.split()
        arr=nup.asarray(first,dtype=int)
        g=compute_height(n,arr)
        print(g)
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,

# so raise it here for this problem. Note that to take advantage

# of bigger stack, we have to launch the computation in a new thread.

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
