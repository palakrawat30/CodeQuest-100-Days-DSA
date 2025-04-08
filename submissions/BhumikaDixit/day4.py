num = int(input("Enter a number: "))
sum = sum(int(i) for i in str(num))
print(f"Sum of digits: {' + '.join(str(num))} = {sum}")