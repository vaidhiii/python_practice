keys=["name","age","city"]
values=["Elsa",16,"Arendelle"]
print("Lists:\n", keys, "\n", values)
my_dict={}

for i in range(len(keys)):
    my_dict[keys[i]]=values[i]
print("Dictionary : ")
print(my_dict)