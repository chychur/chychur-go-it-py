first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gcd = first if first < second else second
conter = 0

while first % gcd == 0 and second % gcd == 0:
    result = gcd - counter
    counter = counter + 1
    print(result)
