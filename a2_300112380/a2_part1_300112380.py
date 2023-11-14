import math
import random


def elementary_school_quiz(flag, n):
    # Your code for elementary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    #
    # Preconditions: flag is 0 or 1, n is 1 or 2

    
    if flag == 0:
        if n == 0:
            return
        
        number_of_correct_answers = 0

        for question in range(n):
            x = random.randint(0, 9)
            y = random.randint(0, 9)

            answer = input("What is " + str(x) + " - " + str(y) + "?")
            if int(answer) == (x-y):
                number_of_correct_answers = number_of_correct_answers + 1
        
        if number_of_correct_answers == n:
            print('Congratulation ' +name+ ', you will probably get an A tomorrow!')
        elif number_of_correct_answers > n/2:
            print('You did okay,' +name+ 'but I know you can do better.')
        elif number_of_correct_answers == 0:
            print('I think you need some more practice ' +name+ '.' )

    elif flag == 1:
        number_of_correct_answers = 0

        for questions in range(n):
            x = random.randint(0, 9)
            y = random.randint(0, 9)

            answer = input(f'What is {x}^{y}?')
            if int(answer) == (x**y):
                number_of_correct_answers = number_of_correct_answers + 1

        if number_of_correct_answers == n:
            print('Congratulation ' +name+ ', you will probably get an A tomorrow!')
        elif number_of_correct_answers > n/2:
            print('You did okay,' +name+ 'but I know you can do better.')
        elif number_of_correct_answers == 0:
            print('I think you need some more practice ' +name+ '.' )


def high_school_quiz(a,b,c):
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function

    print(f"The quadratic equation {a}x^2+{b}x+{c}")
    print("has the following real roots:")

    root1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    root2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

    print(f"{root1} and {root2}")


# main

# your code for the welcome tmessage goes here

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status=='1':
    # your code goes here
    flag = input(f"{name} what would you like to practice? Enter \n0 for subtraction or\n1 for exponentiation")
    num_of_ques = input("How many practice questions would you like to do? Enter 0, 1, or 2:")
    elementary_school_quiz(int(flag), int(num_of_ques))

elif status=='2':

    # your code for welcome message
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        # your code to handle varous form of "yes" goes here

        if question.strip()!="yes":
            flag=False
        else:
            print("Good choice!")
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            # the three coefficients the pupil entered
            a = int(input("Enter a number the coefficient a:"))
            b = int(input("Enter a number the coefficient b:"))
            c = int(input("Enter a number the coefficient c:"))

            print(high_school_quiz(a,b,c))

            go_again = input("Would you like to go again?")
            if go_again == 'no':
                flag=False
                print('Goodbye')


 
else:
    # your code goes here
    
    print("Good bye "+name+"!")

    #print is sufficient to close the commands and program.
