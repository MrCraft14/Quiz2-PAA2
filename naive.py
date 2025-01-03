import random

# Set seed
random.seed(40)

# Generate 50 bilangan random
data = [random.randint(0, 100) for _ in range(50)]
print("Data:", data)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted_data_naive = bubble_sort(data.copy())
print("Naive Sorted Data:", sorted_data_naive)