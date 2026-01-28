import re
pattern=r"^(?=.*[A-Z])(?=.*\d).{8,}$"
words=["123Xy#i","A95843nvnfPjfndj","sdfjfnfekjkinhji123","AsduAPUiine fij456"]
def fun(words):
    for word in words:
        if bool(re.findall(pattern,word)):
            print(word,"Valid Password")
        else:
            print(word,"Invalid Password")
print(fun(words))