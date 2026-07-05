print("Sum of numbers from 1 to n")
n=int(input("Enter number till you want sum:"))
total=0
for i in range(1, (n+1)):
    total= total+i
    i+=1
print(total)