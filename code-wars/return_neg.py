# https://www.codewars.com/kata/55685cd7ad70877c23000102/


def make_negative( number ):
    if number < 0:
        return number
    return number * -1

# or simply
def make_negative( number ):
    return -abs(number)