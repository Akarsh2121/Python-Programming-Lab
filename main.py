/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#regular expression vowels
import re
pattern=r'[aeiou]'
if re.search(pattern,"bcdfg"):
    print("match found")
else:
    print("not found")