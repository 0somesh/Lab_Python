def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 9    ## input number
result = factorial(number)
print(f"The factorial of {number} is {result}")