# https://turjachaudhuri.wordpress.com/2013/12/15/facebook-hacker-cup-2013-balanced-smileys/
# https://www.facebook.com/notes/facebook-hacker-cup/qualification-round-solutions/598486173500621


def balanced(s):
    paren = ''
    colon = False

    for i in range(len(s)):
        if s[i] == ':':
            colon = True
            continue
        elif s[i] == '(':
            if colon is False:
                paren += '('
        elif s[i] == ')':
            if colon is False:
                if paren == '':
                    return 'NO'
                elif paren[-1] == '(':
                    paren = paren[:-1]
        colon = False

    if paren == '':
        return 'YES'
    return 'NO'


# above code works for all but last test case below

# test cases:
# ':(()'
# '):('
# ''
# ':(('
# 'i am sick today (:()'
# 'hacker cup: started :):)'
# ')('
# '(:)'


# official solution, which passes all above test cases
def balanced(s):
    minOpen = maxOpen = 0

    for i in range(len(s)):
        if s[i] == '(':
            maxOpen += 1
            if i == 0 or s[ -1] != ':':
                minOpen += 1
        elif s[i] == ')':
            minOpen = max(0, minOpen - 1)
            if i == 0 or s[i-1] != ':':
                maxOpen -= 1
                if maxOpen < 0:
                    break

    if maxOpen >= 0 and minOpen == 0:
        return 'Yes'
    return 'NO'