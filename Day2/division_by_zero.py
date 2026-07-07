try:
    a=4%0
    print(a)
except ZeroDivisionError:
    print("A number cannot be divided by 0.")