import random
import time
import sys
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)  # Випадковий вибір опорного елемента
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Вибір першого елемента як опорного
        left = [x for x in arr[1:] if x < pivot]
        middle = [pivot] + [x for x in arr[1:] if x == pivot]
        right = [x for x in arr[1:] if x > pivot]
        return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def measure_sort_time(sort_function, arr):
    times = []
    for _ in range(5):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_function(arr_copy)
        end_time = time.time()
        times.append(end_time - start_time)
    average_time = sum(times) / len(times)
    return average_time

sizes = [10_000, 50_000, 100_000, 500_000]
randomized_times = []
deterministic_times = []

# Збільшуємо межу рекурсії, якщо необхідно
sys.setrecursionlimit(1_000_000)

for size in sizes:
    print(f"Розмір масиву: {size}")
    # Генеруємо масив випадкових цілих чисел від 0 до 1_000_000
    arr = [random.randint(0, 1_000_000) for _ in range(size)]

    # Рандомізований QuickSort
    avg_time_randomized = measure_sort_time(randomized_quick_sort, arr)
    randomized_times.append(avg_time_randomized)
    print(f"   Рандомізований QuickSort: {avg_time_randomized:.4f} секунд")

    # Детермінований QuickSort
    avg_time_deterministic = measure_sort_time(deterministic_quick_sort, arr)
    deterministic_times.append(avg_time_deterministic)
    print(f"   Детермінований QuickSort: {avg_time_deterministic:.4f} секунд\n")

# Побудова графіка
plt.plot(sizes, randomized_times, marker='o', label='Рандомізований QuickSort')
plt.plot(sizes, deterministic_times, marker='s', label='Детермінований QuickSort')
plt.xlabel('Розмір масиву')
plt.ylabel('Середній час виконання (секунди)')
plt.title('Порівняння алгоритмів QuickSort')
plt.legend()
plt.grid(True)
plt.show()
