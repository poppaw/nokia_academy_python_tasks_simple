### Create function that calculates Fibonacci sequence for given N:
      # Fib(0) == 0
      # Fib(1) == 1
      # Fib(N) == Fib(N-1) + Fib(N-2)

# **************
# Do it with iteration
# **************
# place your code here:


def fibonacci(num):
    if num == 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        fib = [0, 1]
    elif num > 2:
        fib = [0, 1]
        for n in range(2, num):
            fib.append(fib[n - 1] + fib[n - 2])
    else:
        raise ValueError
    return fib


print(fibonacci(5))
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))


# **************
# Do the same but using recursion
# place your code here:
def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def build_fibonacci_sequence(n):
    return [fib_recursive(el) for el in range(0, n)]


print(build_fibonacci_sequence(5))
print(build_fibonacci_sequence(0))
print(build_fibonacci_sequence(1))
print(build_fibonacci_sequence(2))












# **************
# Do the same but using iteration
# **************

# place your code here







