#print fibinacci

def fibonacci_for_loop(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example usage:
fibonacci_for_loop(10)
