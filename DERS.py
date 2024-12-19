# import turtle 
# wn = turtle.Screen()
# alex = turtle.Turtle() 
# alex.forward(150)
# alex.left(90)
# alex.forward(75)

# name = input("please write your name")
# print("welcome " , name )
# print(type(input("this is just for type checking:  ")))
# x = 4.5
# print(type(x)) 
# yaş = input("yaşınızı giriniz :  ")
# print("yaşınızın türü:" type(yaş))


# print(type(input("please  :  ")))

# name = input("please write your name: ")
# print("welcome", name)

# sayı1 = int(input("sayı giriniz"))
# sayı2 = int(input("sayı giriniz"))

# s = 0 
# for I in range (sayı1 ,sayı2 + 1):
#     s = s + I
# print(s)

# print("hello mars")
# print(200%19)
# print(type(200/19))
# print(200%3)
# name =input("yaş")
# print(name)

#  ghdfhgdgfddfööö    
"""
ewarfesgrhdnrrwfeg     SHIFT ALT + a
gdhfnnfge
""" 
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


# def is_leap(year):
#     leap = False
#     if year/4==0:
#       if year/100==0:
#         if year/400==0:
#          print(True)
#     if year/4 !=0:
#      print(True)

#     # Write your logic here
    
#     return leap

# year = int(input())
# print(is_leap(year))

# def is_leap(year):
#     leap = False
#     if year/4==0:
#       if year/100==0:
#         if year/400==0:
#          print(True)
#         else :
#          print(leap)
#       else:
#         print(False)

#     elif year/4 !=0:
#       print(True)
#       return leap
#     # Write your logic here

# year =int(input())
# print(is_leap(year))

# def is_leap(year):
#     leap = False
#     if year%4==0:
#       if year%100==0:
#         if year%400==0:
#           print(True)
#         else :
#           print(False)
#       else:
#        print(True)
#     else:
#       print(False)
      
#     return leap
    
#     # Write your logic here

# year = int(input())
# print(is_leap(year))


# year = int((input()))
# if year%4==0:
#       if year%100==0:
#         if year%400==0:
#           print(True)
#         else :
#           print(False)
#       else:
#        print(True)
# else:
#       print(False)
  
# result=0
# list=[2,5,-1,4,-3,8]
# for ı in list:
#   for j in list:
#     if j<0:
#       result+=1
#       break
# print(result)



# for student_no in range (1,2):
#   midterm = float(input("midterm: "))
#   final = float(input("final: "))
#   no_of_labs = float(input("Number of lab s: "))
#   total_lab=0
  

#   answer = True
#   while answer:
#     lab= float(input("Lab: " + str(lab_no)))
#     total_lab= total_lab+lab
#     x= input("press(e)for exit")
#     if x =="e":
#       answer =False
#   """for lab_no in range (1,no_of_labs +1):,
#   lab= float(input("Lab: " + str(lab_no)))
#   total_lab= total_lab+lab
# lab_avg =total_lab / no_of_labs
# grade= midterm *0.25 +final * 0.5 +lab_avg * 0.25""""


# if grade >= 60:
#   print("Pass")
# else:
#   print("fail")

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
# while number <= 100:
#    print(number)
#    number = number + 1
# print("number : " , number)
# number =0 
# while True:
#    if number % 2 ==0:
#       print(number)
#    if number == 101:
#       break
#    number+=1


   
# students = ["ahmet","onur","mehmet","enes","oğuz"]
# for name in students:
#    if name == "mehmet":
#       print(name ,":", 100)
#       continue
#    print(name, ":" ,50)

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
# # number1=1
# number2=1
# while number1 <6:
#    number2= 1
#    while number2<6:
#       print(f"{number1} x {number2} = {number1*number2}" , end = "\t")
#       number2+=1
#    print()
#    number1+=1

""" a = 47
b = 47
x = abs(10-a)
y = abs(10-b)

if x == y :
    print("0")
elif x > y :
    print(b)
else:
    print(a) """




# def isPerfect(number):
#     s = 0
#     for i in range(1,number):
#         if number % i == 0:
#             s = s +i 
      
#     return s == number   
      
#     # if s == number :
#     #     return True 
#     # else :
#     #     return False

# print(isPerfect(28))



# def isCoprime(x,y):
#     smaller = y
#     if x < smaller :
#         smaller = x



#     c = True 
#     for i in range (2, smaller +1):
#         if x % i == 0 and y % i == 0:
#             c = False
#             break

#     return c

# print(isCoprime(5,25))

# import random

# def print_track(h,t):
#     for i in range(50):
#         if h == t and h == i:
#             print("@", end="")
#         elif h == i:
#             print("H", end="")
#         elif t == i:
#             print("T", end="")
#         else:
#             print("-", end="")
#     print()

# def moveHare(a):
#     x = random.randint(1,100)
#     if x <= 10:
#         a = a + 5
#     elif x <= 30:
#         a = a -1
#     elif x <= 60:
#         pass
#     elif x <= 80:
#         a = a + 1
#     else:
#         a = a + 2
#     if a < 0:
#         a = 0

#     return a

# def moveTortoise(a):
#     x = random.randint(1,100)
#     if x <= 25:
#         a = a - 2
#     elif x <= 60:
#         pass
#     elif x <= 85:
#         a = a + 1
#     else:
#         a = a + 2
#     if a < 0:
#         a = 0

#     return a

# h = 0
# t = 0

# while h < 50 and t < 50:
#    print_track(h, t)
#    h = moveHare(h)
#    t = moveTortoise(t)
#    input()

# print("hare: ", h, "tortoise: ", t)

# if h > t:
#     print("hare wins")
# elif h < t:
#     print("tortoise wins")
# else:
#     print("tie")


# import random
# def number_guess(x):
#     x = random.randit(100,1000)
#     gueeses = []
#     n = 0

    
#     while True:
#         n +=1
#         guesses.append
#         if x == guess :
#             print("YOU WİN")
#             print("YOUR SOCER İS " , n)
#         elif x < guees :
#             print("HİGHER")
#         elif x > guees :
#             print("lower")
        
#     return 
    
    

# guees = int(input())
# print(number_guess(guees))




import random

def readScoreboard():
    f = open("scoreboard.txt")
    sb = {}
    for line in f:
        linearr = line.strip().split("\t")
        name = linearr[0]
        score = linearr[1]
        sb[name] = score
    f.close()
    return sb

def getUsername():
    name = input("Your name: ")
    return name 

def printScoreboard(sb):
    print("----------------SCOREBOARD----------------")
    for k,v in sb.items():
        print(k,v)

def saveScoreboard(sb):
    f = open("scoreboard.txt","w")
    for k,v in sb.items():
        f.write(k + "\t" + str(v) + "\n")
def game(name, sb):
    number = random.randint(100,1000)
    print(number)
    guesses = []
    nog = 0
    
    while True:
        print("Your previous guesses ", guesses)
        g = int(input("Make a another guess: "))
        guesses.append(g)
        nog = nog + 1
        
        if g == 0 :
            return False
        if g == number:
            print("YOU WON")
        elif g > number:
            print("LOWER")
        else:
            print("HIGHER")
        sb[name] = nog
        printScoreboard(sb)
        saveScoreboard(sb)
    return True

 

    
name = getUsername()  
scoreboard = readScoreboard()
printScoreboard(scoreboard)
while True:
    if not game(name,scoreboard):
        break

