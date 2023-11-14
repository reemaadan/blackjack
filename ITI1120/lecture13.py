#two dimensional lists
# each element of the list is its own list
# in order to access the elements of the 2d list, assign to a variable
lst = [ [3,4,5], [4,5,6], [5,6,7]]
'''lst[0] # returns the first list [3,4,5]'''
#EXAMPLE 1 : HOW TO MAKE A 2D LIST (matrix) AND POPULATE IT

m=[]
n=int(input("give me a positive integer: "))
for i in range(n):
    raw=[1]*n #multiply list with an int to create that many items in the list
    m.append(raw)


for raw in m:
    #raw = m[0]
    for item in raw:#outside the inner for loop, use print as a way to manipulate output and create matrix
        print(item, end=" ")
    print()
''' the following is an alternative solution to the above:
for i in range(len(m)):
    for j in range(len(m[i])):
        print((m[i][j], end = " "))

    print()
'''
#gEXAMPLE 2: iven a 2d list in py, is this a diagonal matrix? 
'''Diagonal matrix is a square matrix where the positive diagonal is all 0's'''

def is_diagonal(m):
    '''(2d list of in) ---> bool'''
    #1. m nees to be a square matrix
    #2. all elements off of diagonal have to be 0

    #testing if m is a square matrix
    for i in range(len(m)):
        #m[i]
        if len(m[i]) == len(m):
            return False
    #here we know that m is a square matrix

    #testing all elements off of the diagonal

    for i in range(len(m)):
        #m[i] raw
        for j in range(len(m[i])):
            #m[i][j]
            if m[i][j] != 0 and i != j:
                return False
    #if you make it here
    return True


def frequency(a): #input list of str, output 2d list
    f=[]
    for i in range(len(a)):
        city = a[i]
        flag = False
        for j in range(len(f)):
            #f[j] little list of 2 elements: city, count
            if city == f[j][0]:
                f[j][1] = f[j][1] + 1
                flag = True
        if flag == False:
            


cities= ['mostar', 'melbourne', 'sarajevo', 'mostar', 'paris', 'melbourne', 'budapest', 'melbourne']
#[['mostar', 2], ['melbourne', 3 ], ['sarajevo', 1], ['paris', 1], ['budapest', 1]] is what we want to return
freq = frequency(cities)
print(freq)

