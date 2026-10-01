import os
import timeit
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

from fibonacci import fibonacci_sequence

WORKERS = os.cpu_count()


def fibonacci_naive(k):
    """Return the k-th Fibonacci number using the naive O(2^k) recursion."""
    if k < 2:
        return k
    return fibonacci_naive(k - 1) + fibonacci_naive(k - 2)


def naive_sequence(n):
    """First n Fibonacci numbers, each computed independently (serially)."""
    return list(map(fibonacci_naive, range(n)))


def parallel_naive_sequence(n, executor):
    """First n Fibonacci numbers, each computed independently by a worker pool."""
    return list(executor.map(fibonacci_naive, range(n)))


def time_function(func, *args, repeats=5, number=10):
    """Return the best average time per call of func(*args), in seconds.

    Runs func `number` times per trial and keeps the fastest of `repeats`
    trials, which filters out noise from other programs on the laptop.
    """
    trials = timeit.repeat(lambda: func(*args), repeat=repeats, number=number)
    return min(trials) / number


def report(label, seconds, baseline):
    print(f"  {label:<38}{seconds * 1e3:>10.4f} ms   {baseline / seconds:>8.2f}x")


def compare(n, threads, processes):
    expected = fibonacci_sequence(n)
    assert naive_sequence(n) == expected
    assert parallel_naive_sequence(n, threads) == expected
    assert parallel_naive_sequence(n, processes) == expected

    baseline = time_function(naive_sequence, n)
    print(f"\nFirst {n} Fibonacci numbers (speed-up relative to naive serial):")
    report("efficient recursion (serial)", time_function(fibonacci_sequence, n), baseline)
    report("naive recursion (serial)", baseline, baseline)
    report(f"naive recursion ({WORKERS} threads)",
           time_function(parallel_naive_sequence, n, threads), baseline)
    report(f"naive recursion ({WORKERS} processes)",
           time_function(parallel_naive_sequence, n, processes), baseline)


if __name__ == "__main__":
    # Pools are created once, outside the timed region, so the timings show
    # the cost of the computation and task hand-off, not of starting workers.
    with ThreadPoolExecutor(WORKERS) as threads, ProcessPoolExecutor(WORKERS) as processes:
        compare(20, threads, processes)
        compare(30, threads, processes)
