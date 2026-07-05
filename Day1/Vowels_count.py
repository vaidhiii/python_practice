string="Damon Salvatore"
count=0
vowel="aeiou"
for i in string:
    if i in vowel:
        count+=1
print(f"Total vowels in string : {count}")