'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import re
pattern=r"[\w.-]+@[\w.-]+"
string="Please send your fedback at info@oxford.com"
match=re.search(pattern,string)
if match:
    print("#regular expressions
Email to:",match.group())
else:
    print("no match")
pattern=r"^[0-9]+ .*"
string="12 abc"
match=re.search(pattern,string)
if match:
    print("match")
result=re.findall(r'.',"good going")
print(result)
result1=re.findall(r'\w+',"good going")
print(result1)
result2=re.findall(r'\w+$',"good going")
print(result2)
result3=re.findall(r'\w\w\w',"good going")
print(result3)