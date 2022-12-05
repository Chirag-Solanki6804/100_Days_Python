# Exercise 1: Calculator using Python | Python Tutorial - Day #7

num1=(float)(input("Enter First Number :"));
num2=(float)(input("Enter Second Number :"));
op=(str)(input("Enter opration :"));

if(op=='+'):
    print("addition of",num1,"and",num2,"is =",num1+num2);   # Addition Operator

if(op=='-'):
    print("subtraction of",num1,"and",num2,"is =",num1-num2);  # Subtraction Operator

if(op=='*'):
    print("multiplication of",num1,"and",num2,"is =",num1*num2);  # Multiplication Operator

if(op=="/"):
    print("division of",num1,"and",num2,"is =",num1/num2);  # Division Operator

if(op=="%"):
    print("remainder of",num1,"/",num2,"is :",num1%num2); # Modulus	Operator

if(op=="//"):
    print("the value of",num1,"//",num2,"is :",num1//num2); # Floor division Operator





