'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#count of a number
list1=[]
print("enter the list:")
for i in range(1,10):
    x=int(input())
    list1.append(x)
print("enter the number to be searched:")
y=int(input())
c=0
ind=0
print("index values:")
for i in list1:
    if y==i:
        print(ind)
        c+=1
    ind+=1
print("count :",c)