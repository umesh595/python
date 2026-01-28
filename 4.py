def gen(n):
    i=1
    while i<n+1:
        if(i%3==0 and i%5==0):
            yield i
        i+=1
print(list(gen(40)))