def min_enclosing_circle(r, x_centrepoint, y_centrepoint):
    #check if the radius is negative, if so return 'None'
    if r < 0:
        return 'None'
    #look for the corner of the rectangle enclosed by the circle
    #in the context of the question the circle and rectangle should always meet
    #find the corner of rectangle aka calc the difference in the radius and the centre point
    else:
        x_leftcorner = x_centrepoint - r
        y_leftcorner = y_centrepoint - r

        return (x_leftcorner, y_leftcorner)
    
print(min_enclosing_circle(500, 1000, 2000))


def vote_percentage(results:str):
    #make sure that the fucntion can count the number of str inputs
    
    votes = results.split(" ")
    count_yes = 0
    count_no = 0
    for vote in votes:
        if vote in 'yes':
             count_yes = count_yes + 1
        elif vote in 'no':
            count_no = count_no + 1
    if count_yes > count_no:
        return count_yes/(len(votes))
    else:
        return count_no /(len(votes))
    
print(vote_percentage('yes no no no yes yes yes yes'))
        
def vote_percentage_with_abstained():
    #make sure that the fucntion can count the number of str inputs
    
    results = input("Enter the yes, no, and abstained votes and then press enter:")
    votes = results.split(" ")
    count_yes = 0
    count_no = 0
    count_abstained = 0

    for vote in votes:
        if vote in 'yes':
             count_yes = count_yes + 1
        elif vote in 'no':
            count_no = count_no + 1
        elif vote in 'abstained':
            count_abstained = count_abstained+1
        


    if count_yes > count_no:
        percent_yes = count_yes/(len(votes)-count_abstained)
        if percent_yes == 1:
            return "Unanimous"
        elif percent_yes >= 2/3:
            return "Super majority"
        elif percent_yes >= 1/2:
            return "Simple majority"  
    else:
        percent_no = count_no /(len(votes)-count_abstained)
        if percent_no == 1:
            return "Unanimous"
        elif percent_no >= 2/3:
            return "Super majority"
        elif percent_no >= 1/2:
            return "Simple majority"
    
print(vote_percentage_with_abstained())

