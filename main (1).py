'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#regular expression plural
import re
def pluralize(noun):
    if re.search('[six]$',noun):
        return re.sub('$','es',noun)
    elif re.search('[^aeiousgkprt]h$',noun):
        return re.sub('$','es',noun)
    elif re.search('[aeiou]y$',noun):
        return re.sub('y$','ies',noun)
    else:
        return noun + 's'
list=["bush","fox","toy","cap"]
for i in list:
    print(i,'-',pluralize(i))