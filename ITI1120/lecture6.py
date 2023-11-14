''' notes for today: Assignment 2 is open, available for work.
pdf file REQUIRED for section 1 of A2
we will go over some of the harder questions from assignment 1'''
'''ONE WAY IF STATEMENTS'''
if temperature > 30:
    print('it is hot')
    print('be sure to drink liquids')
print('Goodbye.')
'''TWO WAY IF STATEMENTS'''
if<condition>
    <indented block>
else:
    <indented block>
<non indented block>

if temperature > 30:
    print('it is hot')
    print('be sure to drink liquids')
else:
    print('it is not hot')
    print('bring a jacket')
print('Goodbye.')

'''MUTLIWAY STATEMENTS also elif statements'''
def temperature(t):
    if t>30:
        print('it is hot')
        print('be sure to drink liquids')
    elif t>0:
        print('it is cool')
    else:
        print('it is freezing!')
print('Goodbye.')

def abs(x):
    '''(number)-->number'''
    if x<=0:
        return -x
    else:
        return x
    
'''how would we shorten this?'''
def abs(x):
    if x<0:
        return -x 
    return x
'''or use print() instead of return for these lines'''
''' NOTE that one return statement is good form'''
def abs(x):
    if x<0:
        x = -x 
    return x

def format_age(age):
    '''(int)-->'''
    if age <20:
        return age
    elif age <30:
        return "twenty something"
    elif age<40:
        return "thirty something"
    else:
        return 'ancient'
    
'''WHAT HAPPENS IF WE USE PRINT???'''
def format_age(age):
    '''(int)-->none'''
    if age <20:
        print(str(age))
    elif age <30:
        print( "twenty something")
    elif age<40:
        print ("thirty something")
    else:
        print( 'ancient')

'''it will only print one answer per id statement, but if we change elif to if, it will print one answer per if statement, aka 2 answers/2if statements'''
'''python has an IN operator, which will sift and give a ture/false'''
s = 'September'
'S' in s
True
'E' in s
False
'e' in s
True

'''function and methods are slightly different, to call a method
it must be called in an object oriented way. NOTE STRIP FUNCTION'''
