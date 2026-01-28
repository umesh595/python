def gen():
    i=1
    while i<21:
        if i*i%2!=0:
            yield i*i
    return None
print(list(gen()))        