"""
45 min time limit (N0rdstr0m Interview)

The goal of this challenge is to design a cash register program. You will be given two decimal numbers. The first is the purchase price (PP) of the item. The second is the cash (CH) given by the customer. Your register currently has the following bills/coins within it:
  'PENNY': .01,
  'NICKEL': .05,
  'DIME': .10,
  'QUARTER': .25,
  'HALF DOLLAR': .50,
  'ONE': 1.00,
  'TWO': 2.00,
  'FIVE': 5.00,
  'TEN': 10.00,
  'TWENTY': 20.00,
  'FIFTY': 50.00,
  'ONE HUNDRED': 100.00
The aim of the program is to calculate the change that has to be returned to the customer.
  Input:
Your program should read lines of text from standard input. Each line contains two numbers which are separated by a semicolon. The first is the Purchase price (PP) and the second is the cash(CH) given by the customer.
  Output:
For each line of input print a single line to standard output which is the change to be returned to the customer. In case the CH < PP, print out ERROR. If CH == PP, print out ZERO. For all other cases print the amount that needs to be returned, in terms of the currency values provided. The output should be alphabetically sorted.

Test 1
Test Input Download Test Input15.94;16.00
Expected Output Download Test OutputNICKEL,PENNY
Test 2
Test Input Download Test Input17;16
Expected Output Download Test OutputERROR
Test 3
Test Input Download Test Input35;35
Expected Output Download Test OutputZERO
Test 4
Test Input Download Test Input45;50
Expected Output Download Test OutputFIVE
"""


def register(pp, ch):
    pp = int(pp * 100)
    ch = int(ch * 100)
    change = []

    if ch < pp:
        return 'ERROR'
    if ch == pp:
        return 'ZERO'
    remainder = ch - pp

    while remainder > 0:
        if remainder >= 10000:
            change.append('ONE HUNDRED')
            remainder -= 10000
        elif remainder >= 5000:
            change.append('FIFTY')
            remainder -= 5000
        elif remainder >= 2000:
            change.append('TWENTY')
            remainder -= 2000
        elif remainder >= 1000:
            change.append('TEN')
            remainder -= 1000
        elif remainder >= 500:
            change.append('FIVE')
            remainder -= 500
        elif remainder >= 200:
            change.append('TWO')
            remainder -= 200
        elif remainder >= 100:
            change.append('ONE')
            remainder -= 100
        elif remainder >= 50:
            change.append('HALF DOLLAR')
            remainder -= 50
        elif remainder >= 25:
            change.append('QUARTER')
            remainder -= 25
        elif remainder >= 10:
            change.append('DIME')
            remainder -= 10
        elif remainder >= 5:
            change.append('NICKEL')
            remainder -= 5
        else:
            change.append('PENNY')
            remainder -= 1

    return ','.join(sorted(change))


# in JS, the while check then changes to `(ch - pp) < 1` because numbers in JS are floats (there is no integer)