names=["elsa", "anna", "olaf", "kristoff", "elsa", "swen", "olaf"]
result=[]
for i in names:
    if i not in result:
        result.append(i)
print("Original list : ",names)
print("List after removing duplicates : ",result)