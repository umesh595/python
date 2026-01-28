import time
def timer(fun):
    def wrapper(*args):
        start=time.time()
        result=fun(*args)
        end=time.time()
        print(f"time taken {end-start:.6f} seconds")
        return result
    return wrapper
@timer
def sum_n(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s
print(sum_n(5))