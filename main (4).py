'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#list 1-20 divisible by 2 and 4
div=[]
for i in range(1,20):
    if(i%2==0 or i%4==0):
        div.append(i)
print(div)