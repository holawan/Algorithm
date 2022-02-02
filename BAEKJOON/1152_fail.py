words = input()
words = words.strip(' ')

s = 1 
for word in words :
    if word == ' ' :
        s += 1
print(s)