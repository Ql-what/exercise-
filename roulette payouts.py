from random import randrange
number = randrange(-1, 37)

if 1 > number > -2:
    if number == 0:
        print("""
The spin result in 0...
Pay 0
        """)
    if number == -1:
        print("""
The spin result in 00...
Pay 00
        """)
else:
    if 10 >= number > 0:
        if number % 2 != 0:
            status = ['Red', 'Odd', '1 to 18']
        else:
            status = ['Black', 'Even', '1 to 18']
    if 19 > number >= 11:
        if number % 2 != 0:
            status = ['Black', 'Odd', '1 to 18']
        else:
            status = ['Red', 'Even', '1 to 18']
    if 28 >= number >= 19:
        if number % 2 != 0:
            status = ['Red', 'Odd', '19 to 36']
        else:
            status = ['Black', 'Even', '19 to 36']
    if 37 > number > 28:
        if number % 2 != 0:
            status = ['Black', 'Odd', '19 to 36']
        else:
            status = ['Red', 'Even', '19 to 36']
    print(f'''
The spin resulted in {number}...
Pay {number}
Pay {status[0]}
Pay {status[1]}
Pay {status[2]}
    ''')