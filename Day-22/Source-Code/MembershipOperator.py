# in : to check any variable or constant in a seqence
# Eg: a in variable # where variable name may be any sequence, like list, tuples, etc. 

# not in: it gives true, if specific variable is not existing in specified sequence
# Eg: a not in variable name may be any sequence like list, tuple, etc. 

lst=[1, 3, 4.4, 'f']
tup=(1, 2, 4.4, 'f')
print(1 in lst)
print(10 in lst)

print('f' in tup)
print('fdsafsd' in tup)
print(10 not in tup)
print(1 not in tup)