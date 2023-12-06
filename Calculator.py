#Calculator
class Calcu:
    try:
        num1= int(input('Enter first number: '))
        num2= int(input('Enter second number: '))
    except:
        print('Input wrong pls try again')
    op= input('Enter the operation: ')
    def calc(a,b,o):
        if o == '+':
            print('The addition is: '+(str)(a+b))
        elif o == '-':
            print('The substraction is: '+(str)(a-b))
        elif o == '*':
            print('The multiplication is: '+(str)(a*b))
        elif o=='%':
            print('The remainder is: '+(str)(a%b))
        else:
            print('The coefficient is: '+(str)(a/b))
    print(calc(num1,num2,op))