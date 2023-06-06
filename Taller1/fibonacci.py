
def fibonacci(n):

    fn = [0,1]     # Initialize the list with the first two Fibonacci numbers
   
    for i in range(2,n):   # Generate Fibonacci numbers up to the specified value of n
        next_n = fn[i-1] + fn[i-2]
        fn.append(next_n)
    print(fn)    # Print the Fibonacci sequence
    
if __name__=='__main__':
   fibonacci(10)
           
    