num = int(input("Enter a number "))
sum_digits = 0
for digit in str(num):  # Convert number to string and iterate over each digit
    sum_digits += int(digit)  # Convert digit back to integer and add to sum
print("Sum of digits: ",sum_digits)
