def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

print("Prime Number Finder")
try:
    #input
    user_start = int(input("Enter start value: "))
    user_end = int(input("Enter end value: "))

    #output
    result = find_primes(user_start, user_end)
    print(f"Prime between {user_start} and {user_end}: {result}")

except ValueError:
    print("Enter whole numbers only")