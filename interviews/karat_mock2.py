# Karat practice interview on 8/10/2018 using coderpad.io

# You are building an educational website and want to create a simple calculator for students to use. The calculator will only allow addition and subtraction of positive integers.

# Given an expression string using the "+" and "-" operators like "5+16-2", write a function to find the total.

# Sample input/output:
# "6+9-12" => 3
# "1+2-3+4-5+6-7" => -2



# iterate through and record digits until encounter + or -
# track total calculation
# output total


def calculator(str):
    total = 0
    current = ''
    operation = '+'
    
    for i in range(len(str)):
        if str[i] != '+' and str[i] != '-':
            current += str[i]
        elif str[i] == '+':
            if operation == '+':
                total += int(current)
            else:
                total -= int(current)
            operation = '+'
            current = ''
        else:
            if operation == '+':
                total += int(current)
            else:
                total -= int(current)
            operation = '-'
            current = ''
    if operation == '+':
        total += int(current)
    else:
        total -= int(current)
    return total     

print(calculator("1-2-3-4"))
print(calculator("254"))
print(calculator("6+9-12"))
print(calculator("1+2-3+4-5+6-7"))

# need to add first number, so initialize operation as +
# dont forget to add/subtract final number