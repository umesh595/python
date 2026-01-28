def validate_positive(func):
    def wrapper(*args):
        for i in args:
            if i<=0:
                print("invalid input")
                return
        return func(*args)
    return wrapper
@validate_positive
def prod(a,b):
    return a*b
print(prod(4,5))