# Between Two Sets

# Prompt

# Given two arrays of integers
# Determine all integers that satsfy the following conditions:
    # - the elements of the first array are all factors of the integer
    #   being considered

    # - the integer being considered, is a factor of all elements in
    #  the second array.

# These numbers are referred to as being betweent the arrays (the
# two sets)

# Determine how may of these numbers exist?

def getTotalX(a, b):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    # for the following two lines, make sure to import reduce from functools
    l = reduce(lcm, a)
    g = reduce(gcd, b)

    s= 0
    for i in range(l, g + 1, l):
        if g % 1 == 0:
            s += 1
    return s