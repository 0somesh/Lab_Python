def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def start_program():
    user_input = input("Enter a number to find its factorial ('exit' to quit): ")

    if user_input.lower() == 'exit': #base case
        print("end progeram")
        return
    try:
        number = int(user_input)
        if number < 0:
            print("enter +ve integer")
        else:
            result = factorial(number)
            print(f"factorial of {number} is {result}")
    except ValueError:
        print("invalid input! Please enter a whole number")

    #recursive step
    print("-" * 20)
    start_program()

start_program()