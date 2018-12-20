# Ahmed Akhtar
# Virtual Assistant - Python

# Importing Date and Time Module
import datetime

# Putting Date and Time into a variable
now = datetime.datetime.now()

# Putting the input into a variable
entry = input()

# Greetung the User
if 'Hello' in entry or 'Hey' in entry or 'Hi' in entry or 'Wassup' in entry or 'Yo' in entry:
    print('Hello I am Oracle. Your Virtual Assitant')

# Calculator
elif '+' in entry:
    x = entry[0]
    y = entry[2]
    x = int(x)
    y = int(y)
    print(x + y)

elif '-' in entry:
    x = entry[0]
    y = entry[2]
    x = int(x)
    y = int(y)
    print(x - y)

elif '*' in entry:
    x = entry[0]
    y = entry[2]
    x = int(x)
    y = int(y)
    print(x * y)

elif '÷' in entry or '/' in entry:
    x = entry[0]
    y = entry[2]
    x = int(x)
    y = int(y)
    print(x / y)

# Date and Time
elif 'time' in entry or 'date' in entry:
    print("Current year: %d" % now.year)
    print("Current month: %d" % now.month)
    print("Current day: %d" % now.day)
    print("Current hour: %d" % now.hour)
    print("Current minute: %d" % now.minute)
    print("Current second: %d" % now.second)
    print("Current microsecond: %d" % now.microsecond)

# Contact Info
elif 'contact' in entry:
    print('My Facebook is facebook.com/ahmed.akhtar5')

# Default Answer
else:
    print('Im sorry I don\'t seem to understand.')