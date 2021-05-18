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