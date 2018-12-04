# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = int(input("Enter a number to check if it is even or odd: "))
divide = int(input("Enter a number to check if it divides evenly into the previous input: "))

if number%2==0 and number%4==0:
    print('\n' + str(number) + ' is an even number and a multiple of 4.')
elif number%2==0:
    print('\n' + str(number) + ' is an even number.')
else:
    print('\n' + str(number) + ' is an odd number.')
    
result = number / divide
    
if number%divide==0:
    print(str(number) + ' divides evenly by ' + str(divide) + ' and the result is ' + str(result))
else:
    print(str(number) + ' does not divide evenly by ' + str(divide) + '.')

