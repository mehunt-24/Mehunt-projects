num1 = int(input("Enter a number: "))
num2 = int(input("Enter the other number: "))
sign = input('Enter the sign for calculation: ')
if sign == '+':
    print('The Answer is: ', num1+num2)
elif sign == '-':
    print('The Answer is: ', num1-num2)
elif sign == '*':
    print('The Answer is: ', num1*num2)
elif sign == '/':  
    print('The Answer is: ', num1/num2)
else:
    print('Enter the symbol of the calculation')
