x = int(input('Enter the x:\n'))
y = int(input('Enter the y:\n'))

try:
    print(x/y)
except ZeroDivisionError:
    print("y cant't be zero")