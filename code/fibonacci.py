def fibonacci_sequence(n):
    """Return the first n Fibonacci numbers, built recursively without loops.

    Each call builds the sequence for n - 1 and appends one new term (the sum
    of the last two), so each number is computed exactly once: O(n) time,
    rather than the O(2^n) of the naive fib(n - 1) + fib(n - 2) recursion.
    """
    if n <= 2:
        return [0, 1][:n]
    sequence = fibonacci_sequence(n - 1)
    sequence.append(sequence[-1] + sequence[-2])
    return sequence


if __name__ == "__main__":
    fib = fibonacci_sequence(20)
    print(*fib, sep=", ")
