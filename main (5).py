'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#regular expressions telephone
import re
list=['7838456789','1234567890','7894561231','9618242748']
for i in list:
    result=re.findall(r'[7-9]{1}[0-9]{9}',i)
    if result:
        print(result,end=" ")