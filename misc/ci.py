def compound_interest():
    principal = int(input('Please enter your inital deposit: $'))
    rate = int(input('Please enter the expected interest rate: '))
    rate = rate / 100
    time = int(input('Please enter the number of years it will be saved: '))
    time += 1
    compound = input('How many times is the interest compounded yearly?: ')

    print(f'Year  Amont on deposit')

    for time in range(1, time):
        formula = principal * (1.0 + rate) ** time
        print(f'{time} {formula}')


def start():
    print('Lets start compounding your interest')
    compound_interest()

start()