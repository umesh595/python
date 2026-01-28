import re
nums=[1,2,3,4,5]
iterable=filter(lambda x:x*x%2==0,nums)
even=map(lambda x:x*x,iterable)
print(list(even))