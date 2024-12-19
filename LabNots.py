# name=input("please write your name: ")
# print("welcome",name)

# print(type(input("this is just for type checking")))

# age=int(input("please write your age: "))
# future_age=age+10
# print(future_age)

# yaş = input("yaşınızı giriniz :  ")
# print("yaşınızın türü:" type(yaş))

# print(type(input("please  :  ")))


# number1=input("please write a number: ")
# number2=input("please write another number: ")
# sum=int(number1)+int(number2)
# print(sum)


# not1=float(input("1.notu giriniz: "))
# not2=float(input("2.notu giriniz: "))
# not3=float(input("3.notu giriniz: "))
# ortalama=(not1+not2+not3)/3
# print(ortalama)


"""
this is a multiline comment in python       SHIFT + ALT + A
                                            Ctrl + K + C/U
"""
'''
this is a multiline comment in python
'''
"""  print("comments are fun!") # this line print out a string """
# message = "hello world"
# number = 10
# pi = 3.14
# is_active = True

# print("message")
# print("number")
# print("pi")
# print("is_active")

# import turtle 
# wn = turtle.Screen()
# alex = turtle.Turtle() 
# alex.forward(150)
# alex.left(90)
# alex.forward(75)

# lecture = "introduction to programming I"
# print(lecture)
# print(type(lecture))
# lecturer = "ali"
# print(lecturer)
# print(type(lecturer))
# number_of_students = 60
# print(number_of_students)
# print(type(number_of_students))
# average_grade_of_quizzes = 0.2
# print(average_grade_of_quizzes)
# print(type(average_grade_of_quizzes))
# can_they_pass = False 
# print(can_they_pass)
# print(type(can_they_pass))
# can_they_pass = "geçebilirler"
# print(can_they_pass)
# print(type(can_they_pass))

# number1 = int(input("give me the first number:  "))
# number2 = int(input("give me the second number:  "))

# total = number1 + number2 
# print("total is : " ,total)
# print(type(number1))
# print(type(number2))
# print(type(total))

# total_of_bool = True + False 
# print(total_of_bool)
# print(type(False))

# total=int(number1)+int(number2)
# print(type(number1))
# print(type(number2))
# print(type(total))
# print("total is" , total)

# a=10
# b=4
# c="---"

# mul=a * b
# print("mul: ", mul)

# rep=a * c 
# print("rep: ", rep)

# float_div=a/b
# print("float_div: ", float_div)

# integer_div=a//b
# print("integer_div: ", integer_div)

# 0 bölüm division by zero

# print(True and False)
# print(False and True)
# print(False and False)
# print(True and True)
# print(False or not False)

# note="it is not possible"

# a=True
# print(type(a))

# for i in range(1, n+1):
#    print(i, end='')

# for İ in range(0,101):
#    if İ % 2 ==0:
#        print(İ)

# for İ in range(1,10):
#    if İ == 5:
#       break
#    print(İ)

# for İ in range(1,10):
#    if İ == 5:
#       continue
#    print(İ)

# for İ in range(1,101):
#    if İ %2 !=0:
#        continue
#    print(İ)   


# number = 0
# while number <=100:
#    print(number)
#    number = number + 1
# print("number : " , number)

# number =0 
# while True:
#    if number % 2 ==0:
#       print(number)
#    if number ==101:
#       break
#    number+=1


   
# students = ["ahmet","onur","mehmet","enes","oğuz"]
# for name in students:
#    if name == "mehmet":
#       print(name ,":", 100)
#       continue
#    print(name, ":" ,50)

""" students=["Ahmet","Onur","Mehmet","Enes","Oğuz"]
for Name in students:
   if Name=="Mehmet":
      print(Name,":",100)
   else: #iki defa mehmet yazmaması için else kullandık
      print(Name,":",50) """

# for i in range(1,4):
#    for j in range(1,4):
#       print(f"({i},{j})" , end = "")
#    print()
   
# for i in range(1,6):
#     for j in range(1,6):
#         print(f"({i} x {j} = {i*j})" , end = "\t")
#     print()

# i=1
# j=1
# while i<6:
#    j=1
#    while j <6:
#      print(f"({i} x {j} = {i*j})" , end = "\t")
#      j+=1
#    print()
# i+=1



# number1=1
# number2=1
# while number1 <6:
#    number2= 1
#    while number2<6:
#       print(f"{number1} x {number2} = {number1*number2}" , end = "\t")
#       number2+=1
#    print()
#    number1+=1

# how_much = int(input("how much money do you have in your bank account? "))
# real_estate = int(input("How many house do you have in Kötekli? "))
# car = input("Do you have car? ")

# threshold_money = 100000
# threshold_house = 5

# if how_much > threshold_money and real_estate > threshold_house and car == "Yes" :
#     print("You donr have to work all day long ")
# elif how_much > 50000 and (car =="yes" or car =="yes"):
#     print("You have to work one day in a week!")
# else:
#     print("You are so poor ypu have to work to live")


# number = int(input("give me number"))

# if number >= 200: 
#    print ("price is 2.000.000")
# elif 150 < number < 200:    
#    print("price is 1.200.000")
# elif 110 < number <= 150:
#    print("price is 700.000")
# elif 90 < number <= 110:
#    print("price is 500.000")
# elif 75 < number <= 90:
#    print("price is 350.000")    
# elif 60 < number <= 75:
#    print("price is 200.000")
# else :
#    print("not found ")




# def myAbs(num):
#     if num < 0 :
#         return -num
#     else :
#         return num

# absValue = myAbs(5)
# print(absValue)

# def eşitlik(x,y,z,d,e):
#     if x == y or x == z or x == d or x == e or y == z or y == z or y == d or y == d or z == d or z == e or d == e :
#         return ("equal")
#     else :
#         return ("not equal")
    
# test = eşitlik(1, 2, 3, 4, 5)
# print(eşitlik)
      
# print("A","B")
# print(1,2)

# print("A" +"B")
# print(1+2)

# a= "A"
# b= "B"
# print(a+" "+b)

# number1 = 5
# number2 = 4 
# total = number1 + number2  

# notFormattedString = str(number1) + " + " str(number2) + " = " +  str(total) 
# print(notFormattedString)
# formattedString = f"{number1} + {number2} = {total}"
# print(formattedString)

# secondFormatted = "{} + {} ={}".format(number1,number2,total)
# print(secondFormatted)

"""TERNARY CONDİNATİONALS """
# a = 10
# if a > 10:
#    print("greater")

# else :
#    if a >5:
#       print("5")
#    else:
#       print("smaller")

# print("greater" if a > 10 else "5" if a > 5 else "smaller" )




# def myAbs(number):
#    if number < 0:
#       print(-number)
#       return 
#    print(number)

# myAbs(-5) 

# def myAbs(number):
#    if number < 0:
#       return -number
#    return number

# myAbs(-10) 

"""CHECK İD NUMBER """
# id_number =int(input("please write your id number :"))
# x =id_number
# a = 0

# for i in range(1,11):      
#     y = id_number//10  
#     id_number = y
#     if id_number > 10:
#         z = id_number % 10
#         a = a + z
#     else:
#         a = a + id_number

# eleventh = a % 10
# t = x % 10     

# if eleventh == t:
#          print("true")
# else :
#          print("false")


# def function(x):
#    sum=0
#    for j in range(x+1):
#       sum+=j
#    return sum
# print(function(5))
   
   
# def function1(x):
#    sum=0
#    while sum <= x:
#       sum+=1
#    return sum
# print(function1(5))



# def triangularFor(number):
#    result=0
#    for i in range(number,0,-1):
#       result += i
#    return result
# print(f"Triangular: {triangularFor(10)}")

# def triangularWhile(number):
#    result=0
#    while (number > 0):
#       result += number
#       number -=1
#    return result
# print(f"triangular: {triangularWhile(10)}")


# def triangularRecursive(number):
#    if number == 1:
#       return 1
#    return number + triangularRecursive(number-1)

# print(f"triangular: {triangularRecursive(10)}")
            

# def for1(number):
#    for i in range(number):
#       print(i)
# for1(101)
   
# def recursive(number,number1,asc):
#    if asc:
#       if number == number1+1:
#          return
#       print(number,end=" ")
#       return recursive(number+1,number1,asc)
#    else: 
#       if number == number1+1:
#          return
#       print(number,end=" ")
#       return recursive(number,number1-1,asc)


# recursive(0,10,True)
# print()

# def recursive(start,end,asc):
#     if asc:
#         if start == end:
#             return
#         print(start+(start+1),end=" ")
#         return recursive(start+1,end,asc)
        
#     else:
#         if start == end:
#             return
#         print(end+(end-1),end=" ")
#         return recursive(start,end-1,asc)
        
# recursive(0,10,False)
# print()


# def pairwise(start,end):
#     if start == end :
#         return
    
#     total = start+ (start+1)
#     print(total, end=" ")
#     return pairwise(start+1,end)
# pairwise(0,10)
# print()

"""
casting = tuple([1,2,3,4,5])
emptyTuple = ()
emptyTuple = tuple()
myTuple = (1,2,3,4,4,5)

print(type(casting))
print(myTuple.index(3))
print(myTuple.count(4))
"""

import random

# #a= [random.randint(0,35) for i in range(30)]
# temps=[5,10,15,24,21,19,18,15]
# # for i in range(30):
# #    a.append(random.randint(0,35))
# print(temps)
# def biggest_difference(tempss):
#    max_temp = 0
#    for temp in tempss:
#       if temp > max_temp:
#          max_temp = temp
#    print(max_temp)
#    max_index = tempss.index(max_temp)
#    print(max_index)
   
#    max_diff = 0
#    for i in range(max_index,len(tempss)-1):
#       # print(i,i+1)
#       # print(tempss[i],tempss[i+1])
#       difference = abs(tempss[i]-tempss[i+1])
#       if difference > max_diff:
#          max_diff = difference
#    print(max_diff)
      


# biggest_difference(temps)

number = random.randint(0,1000)

guess = int(input("Please give a number to guess :"))
counter = 1


while guess != -1 and number != guess and counter < 10:
   counter += 1

   
   if number > guess:
      print("higher")
      
   else:
      number < guess
      print("lower")
   guess = int(input("Please give a number to guess :"))

if guess == -1:
   print("thank you for playing this game")

if counter > 10:
   print("You lost the game")

if guess == number:
   print("you won the game")



