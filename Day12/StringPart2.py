# Strings Slicing and Operations on Strings in Python | Python Tutorial - Day #12

names="chirag,hiral";
# length=len(names);
print(len(names));
print(names[0:6]); # it give 0to5 char
print(names[7:12]);

#negative slicing
#if you want to remove char from last 
print(names[0:-5]); #here hiral is removed from last
#explain::print(names[0:len(names)-5]);

print(names[-2:-3]);
#names[len-2:len-3];
# names[12-2:12-3];
# names[10:9]; #return nothing 

print(names[-5:-1]); #return hira

nm="Harry";
print(nm[-4:-2]); #it means nm[5-4:5-2] =>nm[1:3] =>here 1 is include and 3 is exclude=>means return char 1 and 2 not 3