# NUMBER LINE JUMPS

# PROMPT

# Given two kangaroos on a number line ready to jump in the positive 
# direction
    # - 1st kangaroo starts at location x1 and moves at v1 meters per jump.
    # - 2nd kangaroo starts at location x2 and moves at v2 meters per jump.

    # - figure out a way to get both jkangaroos at the same location at the 
    # same time. If this is possible, return 'YES', otherwise 'NO'
function kangaroo(x1, v1, x2, v2):
    # use an if/else statement
        # as long as v1 is greater than v2 AND the remainder of
        # x2-x1 divided by v2-v1, is 0, then return a "YES"
        if (v1 > v2) and ((x2-x1) % (v2-v1) == 0):
            return "YES"
        else:
            return "NO"