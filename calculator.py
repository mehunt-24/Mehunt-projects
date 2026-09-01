num1 = int(input("enter a number"))
num2 = int(input("enter the other number"))
sign = input('')
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
