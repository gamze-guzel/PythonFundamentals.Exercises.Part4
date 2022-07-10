def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result
while True:
    number = int(input("Enter a number!"))
    print(factorial(number))
