i# a=complex(8,2)
# print(a)
# b= True
# c="hemant"
# d= none
# print("the type of a",type(a))
# print("the type of b",type(c))
# print("the type of c",type(c))
# print("the type of d",type(d))

# a=50
# b=3
# print("the value of",a,"+", 3 , "is:",a+b)
# print("the value of",a,"-", 3 , "is:",a-b)
# print("the value of",a,"*", 3 , "is:",a*b)
# print("the value of",a,"/", 3 , "is:",a/b)
# print("the value of",a,"%", 3 , "is:",a%b)
# print("the value of",a,"//", 3 , "is:",a//b)
# a="13"
# a=13
# b="5"
# b=5
# print(a+b)
# string="15"
# number=7
# string_number=int(string)
# sum=number+string_number
# print("the sum of both number is:",sum)

# x=input("enter your first number")
# y=input("enter you second number")
# print(x + y)
# print(int(x) +int(y))
# print(int(x)-int(y))
# print(int(x)*int(y))
# print(int(x)/int(y))
# print(int(x)//int(y))
# print(int(x)%int(y))
# print(int(x)**int(y))
# name="hemant"
# print("hello"+name)
# aplle='''hello harry
# i am intelligent 
# how was everyone'''
# print("lets use a for loop\n")
# for character in aplle:
#     print(character)
#     print(aplle[0:5])
# names="hemant"
# len1=len(names)
# # print("hemant is a",len1,
# #       "letter word")
# print(names[-3:-1])
# nm="harry"
#indetemation________space in vs to change block
# print(nm[-4:-2])
# a="hemant!!!!!!!!!"
# print(len(a))
# print(a.upper())
# print(a.lower())
# print(a.rstrip("!"))
# blogheading="introduction to js"
# print(blogheading.capitalize())
# a=int(input("enter your age"))
# print("your age is:",a)

# if(a>18):
#     print("you can drive")
# else:
#     print("you cannot drive") 
# import time
# timestamp = time.strftime('%H,%M,%S')
# print(timestamp)
# timestamp= time.strftime('%H')
# print(timestamp)
# timestamp=time.strftime('%M')
# print(timestamp)
# timestamp=time.strftime('%S')
# print(timestamp)
# colors=["RED","GREEN","yellow","ORANGE","WHITE"]
# for  color in colors:
#     print(color)
#     for i in color:
#         print(i) 

# for k in range(1,50000,500):
#     print(k)


# for i in range(3000):
#     print(i)

# i=0
# while(i<3000):
#     print(i)
#     i=i+1


# for i in range(13):
#     print("5 X",i+1,"=", 5* (i+1))
#     if (i==10):
#         break
# i=0
# while True:
#     print(i)
#     i=i+1
#     if(i%100 ==0):
#         break
from statistics import mean


def calculateGmean(a, b):
    mean =(a*b)/(a+b)
print(mean)
a=77
b=88
calculateGmean(a,b)