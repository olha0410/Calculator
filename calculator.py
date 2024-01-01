def main():
    
    print('User, what do you want to do?')
    print(' +')
    print(' -')
    print(' *')
    print(' /')
    print(' sqrt')

    op = input().strip()
    

    if op not in ['+', '-', '*', '/', 'sqrt']:
        print('Something is wrong.')
        exit()

    print('You chose', op)
    
    result = 0

    if op in ['+', '-', '*', '/']:
        num1 = float(input('Type the first number: '))
        num2 = float(input('Type the second number: '))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2  

    # Since we already checked if the operation the user choosed is in the handled operations, we can just put an else instead of a elif.
    else:
        num = float(input('Type a number: '))
        import math
        result = math.sqrt(num)

    print('The result: ', result)

if __name__ == "__main__":
    main()
