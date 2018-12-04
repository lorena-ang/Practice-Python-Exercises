# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. 
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.Print out that many copies of the previous message on separate lines.

import datetime
get = datetime.datetime.now()
name = input('Enter your name:\n')
age = int(input('Enter your age:\n'))
copies = int(input('Desired copies of result:\n'))
today = get.year
future = (100-age) + today
print(copies * ("Hello %r. Since your current age is %r, you will turn 100 in the year %r\n"
    %(name,age,future)))

