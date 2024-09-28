# Identity Operator: checking identity of two variables. 
# 'is' and 'is not'
# 'is' is used to check variables on boths sides of operator, same object or not
# we can find their identities/address using id method. 

print("Identity Operator in Python")
x=30
y=10
print(id(x))
print(id(y))
print(x is y)
print(y is x)