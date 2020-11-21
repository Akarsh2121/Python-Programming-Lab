'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
dict={'Roll_no':'19h61a0524','Name':'Tharun','Course':'B.tech'}
print(dict)
dict1={x:2^x for x in range(1,10)}
print(dict1)
print(dict['Roll_no'])
print(dict['name'])
print(dict['course'])
dict['marks']=95
print(dict)
dict['course']='bsc'
print(dict)
del dict['marks']
print(dict)
dict.clear()
print(dict)
del dict
print(dict)