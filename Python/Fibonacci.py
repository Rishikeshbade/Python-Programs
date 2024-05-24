def fibonacci(n):
    
    fib_series = [0, 1] 
    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term) 

    return fib_series


n_terms = 10
fibonacci_series = fibonacci(n_terms)
print(f"The first {n_terms} terms of the Fibonacci series are: {fibonacci_series}")
