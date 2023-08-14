import time
# last as a pivot

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
start_time = time.perf_counter()
quick_sort(input_array, 0, len(input_array) - 1)
end_time = time.perf_counter()
execution_time = end_time - start_time  
print(f"Function execution time  {execution_time:.6f} seconds")

print(input_array)



#------------------------------------------------------------------------------------------------

# Firs as a pivot


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]  
    i = low + 1
    
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1


input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
start_time = time.perf_counter()
quick_sort(input_array, 0, len(input_array) - 1)
end_time = time.perf_counter()
execution_time = end_time - start_time  
print(f"Function execution time  {execution_time:.6f} seconds")

print(input_array)


#------------------------------------------------------------------------------------------------

# Median of three

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    
    mid = (low + high) // 2
    pivot = arr[mid]
    arr[mid], arr[high] = arr[high], arr[mid]  
    i = low
    
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[i], arr[high] = arr[high], arr[i]
    return i


input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
start_time = time.perf_counter()
quick_sort(input_array, 0, len(input_array) - 1)
end_time = time.perf_counter()
execution_time = end_time - start_time  
print(f"Function execution time  {execution_time:.6f} seconds")

print(input_array)

#------------------------------------------------------------------------------------------------

# Randomized

import random

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def randomized_partition(arr, low, high):
    random_index = random.randint(low, high) 
    arr[random_index], arr[high] = arr[high], arr[random_index]  
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[i], arr[high] = arr[high], arr[i]
    return i


input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
start_time = time.perf_counter()
quick_sort(input_array, 0, len(input_array) - 1)
end_time = time.perf_counter()
execution_time = end_time - start_time  
print(f"Function execution time  {execution_time:.6f} seconds")

print(input_array)
