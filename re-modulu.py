import re

str = "Python Kursu: Python Programlama Rehberiniz 40 saat"

result1 = re.findall("Python", str)
result2 = len(result1)
print(result1)
print(result2)

result3 = re.split(" ", str)
print(result3)

result4 = re.sub(" ", "-", str)
print(result4)
result5 = re.sub("\s", "-", str)
print(result5)

result6 = re.search("Python", str)
print(result6)