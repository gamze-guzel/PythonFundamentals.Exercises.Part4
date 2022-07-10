def fibonnaci(n):
    if n<=1:
        return n
    else:
        return(fibonnaci(n-1) + fibonnaci(n-2))
user_n_terms = int(input("Enter a positive integer less than 30: "))

if user_n_terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(user_n_terms):
        print(fibonnaci(i))