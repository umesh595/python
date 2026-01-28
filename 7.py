import re
text="Price is 45.50 and discount is 10"
print(re.findall(r"\d+\.\d+|\d+",text))