num = int(input("Enter a number: "))
sum = 0

temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
    
if num == sum:
    print("This number is an armstrong number.")
else:
    print("This number isn't an armstrong number.")
