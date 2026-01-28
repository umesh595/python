def func(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise ValueError("both should be integers")
        return None
    try:
        value=a/b
        return value
    except ZeroDivisionError:
        print("b cant be zero")
        return None
    finally:
        print("executed")
print(func(6,4))