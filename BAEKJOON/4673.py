def d(x) :
    if x < 10 :
        return x
    else :
        return d(x+x%10+x//10)
print(d(4))
