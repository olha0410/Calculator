def main():
    
    print('User, what do you want to do?')
    print(' +')
    print(' -')
    print(' *')
    print(' /')
    print(' sqrt')

    op = input()

    if (op not in ['+', '-', '*', '/', 'sqrt']):
        print('Something is wrong')
        exit()

    print('You chose', op)

    if op in ['+', '-', '*', '/']:
        num1 = float(input('Type the first number: '))
        num2 = float(input('Type the second number: '))

    result = 0

    if (op == '+'):
        result = num1 + num2
    elif (op == '-'):
        result = num1 - num2
    elif (op == '*'):
        result = num1 * num2
    elif (op == '/'):
        result = num1 / num2
    elif (op == 'sqrt'):
        num = float(input('Type a number: '))
        import math
        result = math.sqrt(num)

    print('The result: ', result)

main()
