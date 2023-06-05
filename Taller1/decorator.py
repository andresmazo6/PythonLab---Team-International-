import time
import random

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the original function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Execution time: {execution_time} seconds")  
        return result
    return wrapper

@timer
def sort_and_print(numbers):
    sorted_numbers = sorted(numbers)  # Sort the numbers
    print(sorted_numbers)

random_numbers = [random.randint(1, 100) for _ in range(10)]  # Generate a list of numbers
sort_and_print(random_numbers)  # Call the function with the random numbers


