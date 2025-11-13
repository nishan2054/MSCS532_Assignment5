import random
import time
from typing import List, Callable


# -----------------------------
# Deterministic Quicksort
# Pivot: first element
# Tail recursion optimization
# -----------------------------

def partition_deterministic(arr: List[int], low: int, high: int) -> int:
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quicksort_deterministic(arr: List[int], low: int, high: int) -> None:
    # Iterative style using recursion only on the smaller side
    while low < high:
        p = partition_deterministic(arr, low, high)

        # Recurse into smaller partition to keep depth small
        if p - low < high - p:
            if low < p:
                quicksort_deterministic(arr, low, p - 1)
            low = p + 1
        else:
            if p < high:
                quicksort_deterministic(arr, p + 1, high)
            high = p - 1


# -----------------------------
# Randomized Quicksort
# Pivot: random element
# Same optimization pattern
# -----------------------------

def partition_randomized(arr: List[int], low: int, high: int) -> int:
    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quicksort_randomized(arr: List[int], low: int, high: int) -> None:
    while low < high:
        p = partition_randomized(arr, low, high)

        if p - low < high - p:
            if low < p:
                quicksort_randomized(arr, low, p - 1)
            low = p + 1
        else:
            if p < high:
                quicksort_randomized(arr, p + 1, high)
            high = p - 1


# -----------------------------
# Helpers for experiments
# -----------------------------

def generate_input(size: int, mode: str):
    if mode == "random":
        return [random.randint(0, size * 10) for _ in range(size)]
    elif mode == "sorted":
        return list(range(size))
    elif mode == "reverse":
        return list(range(size, 0, -1))
    else:
        raise ValueError("Unknown mode")


def time_algorithm(algorithm, arr, repeats: int = 3) -> float:
    total = 0.0
    for _ in range(repeats):
        data = arr.copy()
        start = time.perf_counter()
        algorithm(data, 0, len(data) - 1)
        end = time.perf_counter()
        total += (end - start)
    return total / repeats


def run_experiments() -> None:
    sizes = [1000, 5000, 10000, 20000]
    modes = ["random", "sorted", "reverse"]

    print("Quicksort Performance Comparison")
    print("Times in seconds (averaged)\n")

    for mode in modes:
        print(f"Input type: {mode}")
        print(f"{'n':>8} | {'Deterministic':>15} | {'Randomized':>15}")
        print("-" * 45)
        for n in sizes:
            base_arr = generate_input(n, mode)
            t_det = time_algorithm(quicksort_deterministic, base_arr)
            t_rnd = time_algorithm(quicksort_randomized, base_arr)
            print(f"{n:8d} | {t_det:15.6f} | {t_rnd:15.6f}")
        print()


if __name__ == "__main__":
    run_experiments()
