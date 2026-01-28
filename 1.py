import time 
def time_sliced(gen,interval_ms):
    interval=interval_ms/1000
    start=time.time()
    for item in gen:
        yield item
        if time.time()-start>=interval:
            start=time.time()
            yield
def counter():
    i=0
    while True:
        yield i
        i+=1
g=time_sliced(counter(),0.009)
for i in range(10):
   print(next(g))