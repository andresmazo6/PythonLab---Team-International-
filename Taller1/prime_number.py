def is_prime(number):
    if number < 2:   # Check if the number is less than 2
        return False
    
    # Iterate over numbers from 2 to the square root of the given number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


user_input = int(input("Enter a number: ")) # Take user input


if is_prime(user_input):  # Check if the number is prime
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")
