#comments 
#single line  :-#dipesh is a good boy 
#multiline comments :- 

''' dipesh is a good boy 
gyanii boy 
innocent boy '''

##################################
#variables 
a=1
b=3.45
x=y=z=4
g=4+3j
i=3+7j
h=True
m,n,o=1,3,4
name ="ramuu daii ko kalo kukur ,kalo kholsii kudyoo "
print(a,b,x,y,z,m,n,o,name)
print("kaluko kalo kukur ,",name)
print (f"kaluko kalo kukur hina , ramuko ko ho kukur ,{name}, age={x} ")
 
# take input 
haribol=str(input ("enter your bloiii:"))
print(haribol)
print (f"sum={a+b}")

#data types
print(type(a), type(haribol),type(b),type(g),type(h))

#eg , sum of two complex numbers
print(f"sum ={g+i}")

#type casting
a=5
b=float(a)
c=str(a)
ram="ramram"
print(type(a),type(b),type(c),a,b,c)

#but cant typecast from str to another 
#eg 
# d=int(ram)
# print(type(ram) ,type(d),ram,d)

###############
#operator
# // ------ > (floor division)     for base reminder calcualtion  
# ** ---------> (exponent)     for power calcualtion 
#eg
a=27
b=5
c=3
print(b**c)
print(a//b)

#indentation
# same group of code should be in same line 
#eg          a=23
#              sum=a+24     ----------> wrong format

#conditional 
#if , if - else ,if - elif- else
kukur="kalo"
if(kukur=="kalo"):
    print("ramu loves kalo kukur")
elif(kukur=="seto"):
    print("ramu loves seto kukur")
else :
    print("ramu love sita")

####################
#loop
#for loop , while loop
#for loop 
for i in range(1 ,6):
    print(f" {i}. ramram")            

#while loop 
i=1
while(i<=4):
    print(f"{i} , jay sambhuu sivaji")
    i+=1

