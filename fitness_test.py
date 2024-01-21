'''This is a test branch

I take the user's name

I say, hello (user name), where would you like to workout?

I want this app to recommend a fitness programme to the user, depending on their choices

If the user wants to workout at home, I will recommend them the home workout program

If the user wants to workout at the gym, I will recommend them the gym workout program

If they input the wrong response, I'll say - please type 'gym' or 'home'

APPROACH TO SOLVE THIS PROBLEM:
1. First create a simple bare bones user input program
2. Then create a simple if else program
3. Then look at a program that takes user input and prints conditions based on their input/loops around



'''

#1. Basic user input program

# print("Welcome to the workout app, please enter your name: ")
# name = input ()
# print("Hello, " + name, "where would you like to workout? Type in home, or type in gym")


# #2. Basic if-else program

# a = 200
# b = 33

# if b > a:
#     print("b is greater than a")
# elif a == b: 
#     print("a and b are equal")
# else:
#     print("a is greater than b")  #this program is going to print out "a is greater than b" because 200 is bigger than 33

#3. If-else program with inputs

# a = input("Enter a number: ")
# b = input("Enter another number: ")

# if a>b: 
#     print("First number is largest")
# else:
#     print("Second number is largest")

#4. Now, let's ask the user where they want to workout

# response = input("Type in home or type in gym: ")

# if response == 'gym':
#     print('Gym program')
# elif response == 'home':
#     print('Home program')

# 5. Now, let's ask the user for their name and include their name in the response

# name = input("Type in your name: ")
# print("Hello", name)

# response = input("Home or gym?: ")

# if response == 'gym':
#     print('Gym program')
# elif response == 'home':
#     print('Home program')

#6. Simple while loop program to refresh knowledge

i = 1
while i < 6:
    print(i)
    i += 1 

#i is a value of 1
#since its value is 1, it's going to print numbers 1 to 5
# i += 1 basically increments i by 1 in each iteration
# that is why i is going up from 1 to 2 to 3 to 4 to 5, but stops at 5


