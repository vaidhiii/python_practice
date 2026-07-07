try:
    f = open("questions.txt",'r')
    f.read()
except FileNotFoundError:
    print("This file does not exists.")