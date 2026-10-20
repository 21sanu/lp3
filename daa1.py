
# Fibonacci using Recursive and Non-Recursive Methods

# Non-recursive method
def fibonacci_non_recursive(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()


# Recursive method
def fibonacci_recursive(n):
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Non-recursive Fibonacci series:")
    fibonacci_non_recursive(n)

    print("Recursive Fibonacci series:")
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")
    print()
