vowel="aeiou"
a="this is a computer"
count=0
for letter in a:
    if letter in vowel:
        count+=1
print(count)