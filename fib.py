#!/usr/bin/python3
def fibonacci(n, md={}):
    if n in md:
        return md[n]
    
    if n <= 1:
        md[n] = n
    else:
        md[n] = fibonacci(n - 1, md) + fibonacci(n - 2, md)
    
    return md[n]

def generate_fibonacci_sequence(length):
    sequence = []
    for i in range(length):
        sequence.append(fibonacci(i))
    return sequence

sequence_length = 10  # Change this to the desired length of the sequence
fib_sequence = generate_fibonacci_sequence(sequence_length)
print(fib_sequence)