#if condition:
   # statement(s)
#while will return true as long as the one oart evaluated remains true
#while condition:
   # statement(s)

'''for i in range(10,0,-1):
    print(i)
i=10
while i>0:
    print(i)'''
#the above will only print 10 over and over again because I is one value and thus 
#is always true, and creates an infinite loop

#ps everything a for loop can do, a while loop can do
'''
answer=input("Yes, no do you want to buy a ticket").lower()

while answer!= 'yes' and answer!= 'no':
    print("Input incorrect")
    answer=input("Yes, no do you want to buy a ticket").lower()
#what if a phrase it from an edit based off of what I want?
while not (answer == 'yes' and answer == 'no'):
    print("Input incorrect")
    answer=input("Yes, no do you want to buy a ticket").lower()
#FORBIDDEN from using break statements IN THIS COURSE

s= 'rttofay'

i=0
while s[i] not in "AEIOUaeiou":
    print(s[i])
    i=i+1

i=0
while i<len(s) and s[i] not in "AEIOUaeiou":
    print(s[i])
    i=i+1

#collatz conjecture
# n is even number
#   divide by 2
# otherwise
#    3*n+1

n = 12
12,6,3,10,5,16,8,4,2,1
'''
'''
def collatz(n):
    while n!=1:
        if n%2==0:
            n= n//2
        else:
            n= 3*n+1
    return True
import random
def guessing_game():
    print("I am thinking of a number between 1 and 1000")
    x = random.randint(1,1000)

    tries = 11 #so long as my tries are log base 2(tries) +1 i can guarantee a win
    guess = 0
    tries = tries-1
    while tries != 0 and guess!=x:
        guess = int(input("Try and guess:"))
        if guess < x:
            print("Too low, try again!")
        elif guess > x:
            print("Too High, try again!")
        else:
            print("You got it! Good job")
        tries = tries-1
guessing_game()
'''
''' incomplete example
i=n
while i>=n
'''

#Next lecture!

def maximum(l):
    #input list returns number; precondition: l is not an empty list of numbers
    #given the lsit of number in l, this returns the mx value in the list aka use a for loop
    ''' n = len(l)  here'''
    current_max = l[0] #1
    for item in l:
        if item>current_max: # 1*n
            current_max = item
    return current_max

#lets use a function to find duplicates so that we dont need to do n # of operations
'''
[10,2,11,-4,5.5,10,2,10,5,6] #does this have duplicates, f()returns True
[10,2,11,-4,5.5,5,6]
'''



n=len(l)
def duplicates(l):
    for i in range(n): #this line costs n operations
        #l[i]
        for j in range(n): #n^2
            if l[i] == l[j] and i != j:
                return True #<=1
    return False #<=1

#<=n+2n^2 +2 <= 3n^2+2 = O(n^2)

n=len(l)
def duplicates(l):
    for i in range(n):#1*n
        #i = 0 == n-1
        #i = 1 == n-2
        #i = 2 == n-3 ...
        #i = n-1 aka 0

        # 1+2+3+4...+n <= (n/2)*(n+1)
        for j in range(i+1, n):
            if l[i] == l[j]:
                return True
    return False

def duplicates(l):
    for i in range(n): #n
        if rep>=2: #n
            return True #<=1
    return False

def duplicates_via_sort(l):
    n= len(l)
    l.sort()
    for i in range(n):
        if l[i] == l[i+1]:
            return True
    return False
n*log(n)
print(duplicates_via_sort([1,2,3,4,5,5,6]))