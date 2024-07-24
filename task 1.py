def fibonacci(n):
    # Check if the input is valid
    if n <= 0:
        return "Input should be a positive integer."
    
    # Initializing the first two numbers of the Fibonacci series
    fib_sequence = [0, 1]
    
    # Generating the Fibonacci series up to n terms
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

# Input: Number of terms in the Fibonacci series
n = int(input("Enter the number of terms: "))

# Output: Fibonacci series up to n terms
print(f"Fibonacci series up to {n} terms: {fibonacci(n)}")
