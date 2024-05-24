def fibonacci(n):
    
    a, b = 0, 1
    
    for _ in range(n):
        print(a, end=" ")
        
        a, b = b, a + b

#
num_terms = 10 
fibonacci(num_terms)
