print "Hey, There!"
print "Welcome to....Mental Math Time! This Program will give you 3 Mental Math equations to quickly solve, Hope you get em' right! "
import random
a=random.randint(0,100)
b=random.randint(0,100)
print "Problem #1:",a,"+",b
a1=input("What is the answer?")
if a1==a+b:
    print "\t Great Job!"
else: 
    print "Incorrect Answer, Make sure to review the equation closely!"
a=random.randint(0,10)
b=random.randint(0,10)
print "Problem #2:",a,"x",b
a2=input("What is the answer?")
if a2==a*b:
    print "\t Marvelous Answer!"
else: 
    print "Incorrect Answer, Make sure to review the question closely!"
a=random.randint(0,10)
b=random.randint(0,10)
c=random.randint(0,10)
print "Problem #3:",a,"+",b,"+",c,
a3=input("What is the answer?")
if a3==a+b+c:
    print "\t Brilliant Effort!"
else:
    print "Incorrect Answer, Make sure to review the question closely!"
a=random.randint(0,10)
b=random.randint(0,10)
print "Problem #4:",a,"-",b,
a4=input("What is the answer?")
if a4==a-b:
    print "\t Fantastic!"
else:
    print "Incorrect Answer, Make sure to review the question closely!"
a=random.randint(0,10)
b=random.randint(0,10)
c=random.randint(0,10)
d=random.randint(0,10)
print "Problem #5:",a,"-",b,"x",c,"+",d,
a4=input("What is the answer?")
if a4==a-b*c+d:
    print "\t Fantastic!"
else:
    print "That doesn't seem right, Make sure to remember BEDMAS!"
    