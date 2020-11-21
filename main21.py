dict={'Roll_no':'19h61a0512','Name':'akarsh','Course':'B.tech'}
print(dict)
dict1={x:2^x for x in range(1,10)}
print(dict1)
print(dict['Roll_no'])
print(dict['Name'])
print(dict['Course'])
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