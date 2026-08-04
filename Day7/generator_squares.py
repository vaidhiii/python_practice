def squares():
    for i in range(1,11):
        yield i**2


square=squares()
print(next(square))
print(next(square))
print(next(square))
print(next(square))