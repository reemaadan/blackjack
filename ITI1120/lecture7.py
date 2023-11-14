#SEE IDLE FOR NOTES
def print_vowels(phrase):
    '''(str)-->  None'''
    for ch in phrase:
        if ch == 'a', or ch =='e', or ch=='o', or ch=='u', or ch=='y':
        print(ch)

#OR YOU CAN DO THIS --

def print_vowels(phrase):
    '''(str)-->  None'''
    for ch in phrase:
        if ch in 'aeiouAEIOU':
        print(ch)

#given a phrase return the number of vowels in that phrase
def count_vowels(phrase):
    #(str)--> int
    count =0
    for ch in phrase:
        if ch in 'AEIOUaeiou':
            count = count+1
    return count 
print(count_vowels('helper'))