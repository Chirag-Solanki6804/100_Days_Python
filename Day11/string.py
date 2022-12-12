# Strings in Python | Python Tutorial - Day #11

name="chirag";

print("name :",name);

# ''' or """ is used to write string in multiple lines

text='''
Name:chirag,
Age:18,
College:Darshan University
'''

print("multi-line string:",text);

print(name[0]); #c
print(name[1]); #h
print(name[2]); #i
print(name[3]); #r
print(name[4]); #a
print(name[5]); #g

# print(name[6]); #IndexError: string index out of range

# for in loop

print("iterate String Using For in Loop :"); 

for char in text:
    print(char);
