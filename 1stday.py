# #comments 
# #single line  :-#dipesh is a good boy 
# #multiline comments :- 

# ''' dipesh is a good boy 
# gyanii boy 
# inocent boy '''

# ##################################
# #variables 
# a=1
# b=3.45
# x=y=z=4
# g=4+3j
# i=3+7j 
# h=True
# m,n,o=1,3,4
# name ="ramuu daii ko kalo kukur ,kalo kholsii kudyoo "
# print(a,b,x,y,z,m,n,o,name)
# print("kaluko kalo kukur ,",name)
# print (f"kaluko kalo kukur hina , ramuko ko ho kukur ,{name}, age={x} ")
 
# # take input 
# haribol=str(input ("enter your bloiii:"))
# print(haribol)
# print (f"sum={a+b}")

# #data types
# print(type(a), type(haribol),type(b),type(g),type(h))

# #eg , sum of two complex numbers
# print(f"sum ={g+i}")

# #type casting
# a=5
# b=float(a)
# c=str(a)
# ram="ramram"
# print(type(a),type(b),type(c),a,b,c)

# #but cant typecast from str to another 
# #eg 
# # d=int(ram)
# # print(type(ram) ,type(d),ram,d)

# ###############
# #operator
# # // ------ > (floor division)     for base reminder calcualtion  
# # ** ---------> (exponent)     for power calcualtion 
# #eg
# a=27
# b=5
# c=3
# print(b**c)
# print(a//b)

# #indentation
# # same group of code should be in same line 
# #eg          a=23
# #              sum=a+24     ----------> wrong format

# #conditional 
# #if , if - else ,if - elif- else
# kukur="kalo"
# if(kukur=="kalo"):
#     print("ramu loves kalo kukur")
# elif(kukur=="seto"):
#     print("ramu loves seto kukur")
# else :
#     print("ramu love sita")

# ####################
# #loop
# #for loop , while loop
# #for loop 
# for i in range(1 ,6):
#     print(f" {i}. ramram")            

# #while loop 
# i=1
# while(i<=4):
#     print(f"{i} , jay sambhuu sivaji")
#     i+=1

# #even number using for loop 
# for i in range (1, 20):
#     if(i%2==0):
#         print(i)
          


# #while loop - print even numbers 
# i=0
# while (i<20):
#     if(i%2 ==0):
#         print(i)
#         i+=1

# # #age <0 - not valid  , 100 >age>0 -- 
# age =int (input("enter your age:"))
# while(age <1 or age>100):
#     print("enter valid age:, this is not valid ")
#     age =int (input("enter your age:"))
# else:
#     print(f"you are {age}  years old:")


# #continue
# for i in range (10):
#     if i==6:
#         continue 
#     print (i)

# #break
# for i in range (10):
#     if i==6:
#         break 
#     print (i)

# #string  in loop
# s1="ramu ko kalo kukur ,"
# s2="sita ko kalo kukur "
# for i in s1:
#     print (i)
# print (len(s1))      #for str length
# print (s1 +s2)        #str concat
# print(s1*3)             #repeate same string in n times like N*str 
# print(s1[0])
# print(s1[0:4:2])
# print(s1[8:13])

# if "rato" in s1:
#     print("yes it is there")
# else :
#     print ("no ")

# #cw
# s3= "i ,am, going, to, learn, machin learning"
# # if "mach" in s3:
# #     print ("yes")
# # else :
# #     print ("no")
# # if "gl" in s3:
# #     print ("yes")
# # else :
# #     print ("no")
# # if "o le" in s3:
# #     print ("yes")
# # else :
# #     print ("no")

# s4=s3.split(",")
# print(s4)


# #list and tuple   
# list1 =[1,2,3,6,"python","ai"]
# print (type (list1)) 
# print (len (list1)) 
# for i in list1:
#     print(i)

# #tupe 
# tuple1= (1,2,3,"dipesh")
# # print (type (tuple1)) 
# # print (len(tuple1))
# # for i in  enumerate(tuple1):     #index with elements
# #     print (i) 

# #append
# list1 =[1,6,2,3,6,"python","ai"]
# list1.append(45)          # add elements in last of list 
# print(list1)

# #to add the elements in desired index
# list1.insert(2,"kalo")
# print(list1)

# #remove elements from list 
# list1.remove(6)
# print(list1)
# list1.pop(2)
# list2=[2,4,5,"dipesh"]
# print(list1+list2)
# tuple2=(1,2,3,4)
# print(tuple2+tuple1) 

# #list comprehension
# list_num=[1,2,3,4,5,6,7]
# list_square=[]
# for i in list_num:
#     i=i**2
#     list_square.append(i)
# print (list_square)

# list_num=[1,2,3,4,5,6,7]
# square =[i**2 for i in list_num]
# print(square)

# #print even  numbers from 1 to 20 
# even=[i for i in range(1,21) if i%2==0 ]
# print(even)

# #dictionary in python 
# dict1={"dipesh ":1 , "ramu":2 , "hari":3}
# print (dict1)
# print(dict1.keys(), dict1.values())
# for i in dict1:
#     print (i)
# for i in dict1.values():
#     print (i)
# for i in dict1.items():
#     print (i)

dict1={"dipesh ":[1,2,3,4,5,6,7], "hari":[2,3,4,5,6]}
print(dict1)