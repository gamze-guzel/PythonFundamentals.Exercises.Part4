def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# Constraints
# n >= 0 and n <= 30

while True:
    n = int(input("Please pick a number between 0-30 "))
    print(fibonacci(n))