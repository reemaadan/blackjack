#todays lecture notes, i'll write it down and then make it work as much as possible
#correct and make all functions run tonight, then head to office hours

def only_vowels(s):
    ''' str --> str
    >>> only_vowels(August) (I want it to return a string of ONLY vowels)
    'Auu'
    >>> only_vowels(smrt)
    returns empty string
    '''

    vowels = '' #ch is undefined? defined by string below? how does this work intricately
    for ch in s: # for loops implicitly creates a variable that we name aftert the for'''
        if ch in 'aeiouAEIOU':
            vowels = vowels + ch # 1. why? 2. adds the value of the loop taken from string ch and adds it to empty string vowel?
    return vowels

print(only_vowels('aTublAAqri'))

'''
for VAR_NAME in SEQUENCE #counting is such a famouse sequence, we use range()
BODY of code

for VAR_NAME in range()
body
'''
#s="01234"
#for ch in s:
#    print(ch)

#for i in range(5): #comp starts counting at 0, so it will return 10 numbers, stopping before 5
 #   print(i)

#what if we want the range to count starting at another number? input parameters

for i in range(1, 5):
    print(i)

for i in range(1,11,3): #first two numbers will be the parameters of start and stop, byt the third number will be command of increment by __ number
    print(i)
#for loops create a variable for you implicictly, we named it i here but above it was ch!

#how do we count down? 
'''
select your starting and finishing number, then increment by a negative third number, in order to count in reverse
'''
for i in range(10,0, -1):
    print(i)
print('blastoff!')

# what if we want to be selective? eg. only return even single digits
for i in range(-8,10, 2):
    print(i)

print('remainder eg.')
# or u can do this, but its less efficient
for i in range(10):
    if i%2==0:
        print(i) 

#what if we dont know the length of string we call in range?
#use a lnegth check! len(s) returns number of ch in str, len(s)-1, is the way the comp counts
s= 'asdfghjkl'

for ch in s:
    print(ch)
for i in range(len(s)):
    print(s[i])

#what if our more complex sol'n needs to be selective and skip numbers?
for ch in s:
    print(ch)
for i in range(0, len(s), 2):
    print(s[i])