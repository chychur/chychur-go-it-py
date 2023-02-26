first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

counter = 0

if first == 0 and second == 0:
    print("he GCD of 0 ana 0 is underfin.")
else:
    gcd = min(first, second)
    while True:
        if first % gcd == 0 and second % gcd == 0:
            break
        gcd -= 1
        if gcd == 1:
            gcd = 1
            break
