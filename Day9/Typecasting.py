# Typecasting in Python | Python Tutorial - Day #9

# Implicit Type Casting

# In this,  methods, Python converts data type into another data type automatically. 
# In this process, users don’t have to involve in this process. 

# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts
# b to float
b = 3.0
print(type(b))
 
# Python automatically converts
# c to float as it is a float addition
c = a + b
print(c)
print(type(c))
 
# Python automatically converts
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))


# Explicit Type Casting

stri="100";
num=3;
#sum=stri+num; #TypeError: can only concatenate str (not "int") to str
sum=int(stri)+num; #ans=103
print(sum);



