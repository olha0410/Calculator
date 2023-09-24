# calculator.1
(the user types two numbers and then selects an action to be  taken with them: addition, subtraction, multiplication, division,  exponentiation, square root
def main():
    print('User, what do you want to do?')
    print(' +')
    print(' -')
    print(' *')
    print(' /')
    print(' sqrt')

    op = input()

    if op not in ['+', '-', '*', '/', 'sqrt']:
        print('Something is wrong')
        exit()

    print('You chose', op)

    if op in ['+', '-', '*', '/']:
        num1 = float(input('Type the first number: '))
        num2 = float(input('Type the second number: '))

    result = 0

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    elif op == 'sqrt':
        num = float(input('Type a number: '))
        import math
        result = math.sqrt(num)

    print('\033[94mThe result:\033[0m', result)

if __name__ == '__main__':
    main()
