exp = input('Enter the expression: ').split()
if exp[1] == '+':
    print('The Answer is: ', int(exp[0])+int(exp[2]))
elif exp[1] == '-':
    print('The Answer is: ', int(exp[0])-int(exp[2]))
elif exp[1] == '*':
    print('The Answer is: ', int(exp[0])*int(exp[2]))
elif exp[1] == '/':  
    print('The Answer is: ', int(exp[0])/int(exp[2]))
else:
    print('Enter the symbol of the calculation')
