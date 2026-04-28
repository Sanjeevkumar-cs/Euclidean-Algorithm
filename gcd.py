#Euclid's algorithm to find GCD of two numbers
# Taking input for x and y
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
# Calculating GCD
print("GCD of", x, "and", y, "is:", gcd(x, y)   )