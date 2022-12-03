# Variables and Data Types | Python Tutorial - Day #6

# In Python everything is an object, 
# which means every entity has some metadata (called attributes) and 
# associated functionality (called methods).

# Type of Data
# 1.numberic data ==>>> int,float,complex
# 2.text data ==>>> str
# 3.Boolean data ==>>> True or False
# 4.Sequenced data ==>>> list,tuple
# 5.Mapped data ==>>> dict

number=1234;

num2=123.456

name="chirag";

isOld=True;

d=None;

list1=[2,9.6,"chirag",["gujarat","punjab","Delhi"],["banana","mango"]];
# print(list1);

tuple1={"gujarat","punjab","Delhi"}; #A tuple is a collection which is ordered and unchangeable
# print(tuple1);

dict1={"name":"Chirag","Age":19,"College":"darshan University","canVote":True};
# print(dict1);

print("Type of number",type(number));
print("Type of num2",type(num2));
print("Type of name",type(name));
print("Type of isOld",type(isOld));
print("Type of d",type(d));
print("Type of list1",type(list1));
print("Type of tuple1",type(tuple1));
print("Type of dict1",type(dict1));
