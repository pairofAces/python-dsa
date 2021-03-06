# CLASS PHOTOS 

# Prompt

# It's photo day, and you're the photographer assigned to take class photos. 
# The class that you'll be taking pictures of is an even number of students. 

# All of the students are wearing red or blue shirts. (half and half)

# Your responsibility to arrange the students in two rows with the following
# guidelines:

# - all students with red shirts have to be in the same row
# - all students with blue shirts have to be in the same row
# - each student in the back row needs to be taller than
#   the student in front

# Given two input arrays, one with the heights of the students with red shirts,
# and another with the students with the blue shirts.

#     arrays have the same length, and each height is a positive integer

# Create a function that returns whether or not a class photo that follows
# the guidelines can be taken.

# Complexity Analysis
    # Time: O(n log(n)) time, where (n) is the number of students

    # Space: O(1) space 

def classPhotos(redShirts, blueshirts):
    # sort both input arrays
    redShirts.sort(reverse=True)
    blueshirts.sort(reverse=True)

    # create a variable that will represent the first row's color
        # if/else logic
    if redShirts[0] < blueshirts[0]:
        shirtColorInFirstRow = "RED"
    else:
        shirtColorInFirstRow = "BLUE"
    
    # use a for loop to traverse through the redShirts array
    for i in range(len(redShirts)):
        # set a variable to the element at the (i) position
        redShirtHeight = redShirts[i]
        # set a variable for the blueShirts as well
        blueShirtHeight = blueShirts[i]

        # if/else to make sure the (shirtColorInFirstRow) is equal to "RED" 
        if shirtColorInFirstRow == "RED":
            # now a nested if statement to make sure (redShirtHeight) is greater
            # than or equal to (blueShirtHeight)
            if redShirtHeight >= blueShirtHeight:
                return False
        else:
            # if (blueShirtHeight) is greater than or equal to (redShirtHeight)
            if blueShirtHeight >= redShirtHeight:
                retun False
    
    # after coming out of the previous loops, return True
    return True
