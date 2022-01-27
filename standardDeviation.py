import math 
import csv
with open("data2.csv",newline ="")as f:
    reader = csv.reader(f)
    filedata = list(reader)
data = filedata[0]
n = len(data)
total = 0
for x in data:
    total = total+int(x)
mean = total/n
print(mean)
squaredList = []
for number in data:
    a = int(number)-mean
    a = a**2
    squaredList.append(a)
sum = 0
for i in squaredList:
    sum = sum + i
result = sum/(len(data)-1)
standarddeviaion = math.sqrt(result)
print(standarddeviaion)