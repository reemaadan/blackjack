#[0] question
#[1]-[4] answers
#[5] category
#[6] difficulty

'''
FROM NOW ON, WE DO NOT ASSUME THE USER WILL INPUT THE CORRECT DATA TYPE
'''
import random

def ask_question(q,p):
    print()
    print("Category: ", q[5], "\nDifficulty: ", q[-1])
    print(q[0])
    for i in range (1,5):
        print(i,q[p[i-1]])

def read_answer_raw():
    try: #this is to solve the crash issue of input the wrong data type, this
         #will prevent a crash in your program
    answer = int(input("Answer 1, 2, 3, or 4: "))
    return answer
    except:
        print("Error. PLease enter one of given options as an integer.")
        
def read_answer():
    answer = read_answer_raw()
    while answer not in [1,2,3,4]:#insert condition here
        print("Invalid input. Try Again.")
        answer = read_answer_raw()
        
        
lines=open('quiz.csv').read().splitlines()

questions = []

for line in lines:
    #line contains info about 1 question
    question = line.split("\t")
    questions.append(question)

lives = 3
score = 0

while lives >0:
    q=random.choice(questions)

    p=[1,2,3,4]
    random.shuffle(p)

    ask_question(q)
    ans=read_answer()
#FINSIH LATER
q=questions[0]

ask_question(q)
