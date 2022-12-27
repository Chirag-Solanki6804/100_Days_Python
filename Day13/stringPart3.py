# String Methods in Python | Python Tutorial - Day #13

#String are Immutable 

name="chirag";

print(len(name));

print(name.lower());

print(name.upper());

text="!!!Hello!!!!!!";
print(text.rstrip("!")); 

print(text.replace("Hello","Namaste"));

print(name.replace("c"," "));

citys="porbandar,rajkot,surat,baroda,mumbai,morbi";

print(citys.split(",")); #return list of city

para="hello world from darshan";
print(para.capitalize());

text2="Hello World";
print(len(text2))
print(text2.center(80));
print(len(text2.center(50)));

print(text.count("!")); #return count

print(name.endswith("g")); #return boolean 
print(name.endswith("i",0,3));
print(name.startswith("c"));

print(text2.find("o")); #return -1 if not found
print(text2.index("o")); #return error if not found

str1="chirag123@gmail.com"; #isalnum String means string contain only A-Z or a-z or 0-9
str2="chirag123gmail";
print(str1.isalnum()); #return false
print(str2.isalnum()); #return true

print(text2.islower()); #return false

text3="chirag solanki\n"; #return false 
print(text3.isprintable());

print(text3.title()); #convert text3 into title
text4="Hello World From Darshan"; #return true if all first letter is capitalize
print(text4.istitle());

print(text4.swapcase());
