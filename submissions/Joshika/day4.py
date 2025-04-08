a=int(input("enter a number:"))
sum=0
while(a!=0):
    m=a%10
    sum=sum+m
    a=a//10
print("sum of digits:",sum)
