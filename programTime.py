from datetime import timedelta

def getUnit():
    print()
    print('Unit: ')
    print('1) Minutes')
    print('2) Hours')
    print('3) Days')
    print()
    return int(input('Select with designated number:  '))

def getNumber(unit):
    units = ['minute', 'hour', 'day']
    unit = units[unit-1]

    print()
    print('How many? ')
    amount = float(input('Input a number value:  '))

    return amount, unit

def getInfo():
    print()
    print('How long would you like for this program to run? ')
    unit = getUnit()
    amount, unit = getNumber(unit)
    return amount, unit

def getTimer(amount, unit):
    amount, unit = float(amount), int(unit)
    units = ['minute', 'hour', 'day']
    unit = units[unit-1]

    if unit == 'minute':
        timer = timedelta(minutes=amount)
    elif unit == 'hour':
        timer = timedelta(hours=amount)
    elif unit == 'day':
        timer = timedelta(days=amount)

    return timer
