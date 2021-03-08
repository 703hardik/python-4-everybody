import re
file=open(input("enter a file name:"))
# ex=re.compile('[0-9]+')
sum=0
count=0

for line in file:
    f=re.findall('[0-9]+',line)
    for num in f:

        if int(num)>=0:
            count+=1
            sum+=int(num)
print("there are ",count,"values with a sum =",sum)
