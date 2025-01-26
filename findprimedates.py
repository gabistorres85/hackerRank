
'''In this challenge, the task is to debug the existing code to successfully 
execute all provided test files.

Given two dates each in the format dd-mm-yyyy, you have to find the number of lucky dates between 
them (inclusive). To see if a date is lucky,

Firstly, sequentially concatinate the date, month and year, into a new integer x
erasing the leading zeroes.
Now if  is divisible by either 4 or 7, then we call the date a lucky date.
For example, let's take the date "02-08-2024". After concatinating the day, month and year, we get  
X= 2082024. As  is divisible by 4 so the date "02-08-2024" is called a lucky date.

Debug the given function findPrimeDates and/or other lines of code, 
to find the correct lucky dates from the given input.

Note: You can modify at most five lines in the given code and you cannot add 
or remove lines to the code.

To restore the original code, click on the icon to the right of the language selector.'''

import re
month = []

def updateLeapYear(year):
    if year % 400 == 0:
        month[2] = 29
    elif year % 100 == 0:
        month[2] = 28
    elif year % 4 == 0:
        month[2] = 29
    else:
        month[2] = 28

def storeMonth():
    month[1] = 31
    month[2] = 28
    month[3] = 31
    month[4] = 30
    month[5] = 31
    month[6] = 30
    month[7] = 31
    month[8] = 31
    month[9] = 30
    month[10] = 31
    month[11] = 30
    month[12] = 31

def findPrimeDates(d1, m1, y1, d2, m2, y2):
    storeMonth()
    result = 0
    while (True):
        x = d1
        x = x * 100 + m1
        x = x * 10000 + y1
        if x % 4 == 0 or x % 7 == 0:
            result = result + 1
        if d1 == d2 and m1 == m2 and y1 == y2:
            break
        updateLeapYear(y1)
        d1 = d1 + 1
        if d1 > month[m1]:
            m1 = m1 + 1
            d1 = 1
            if m1 > 12:
                y1 =  y1 + 1
                m1 = 1
    return result

for i in range(1, 15):
    month.append(31)


d1 = 2
m1 = 8
y1 = 2025
d2 = 4
m2 = 9
y2 = 2025

result = findPrimeDates(d1, m1, y1, d2, m2, y2)
print(result)
