'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
list1=[1,2,2,3,4,5,4,4,5,6,7]
print("enter the no.")
x=int(input())
c=0
ind=0
print("index values:")
for i in list1:
    if x==i:
        print(ind)
        c+=1
    ind+=1
print("count :",c)