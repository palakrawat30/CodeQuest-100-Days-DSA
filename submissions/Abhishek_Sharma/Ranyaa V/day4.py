num=int(input("enter a number:"))
original_num=num
digit_list=[]
sum_digits=0
while num>0:
    digit=num%10
    digit_list.insert(0,digit)
    sum_digits+=digit
    num//=10
print("Sum of digits:", "+".join(map(str,digit_list)),"=",sum_digits)