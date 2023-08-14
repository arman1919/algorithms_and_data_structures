import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
            
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result




def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



arr = []
size = 0
for i in range(1000):
    
    arr.append(i)
    
    print(i)
    
    start = time.time()
    for j in range(10000):
        merge_sort(arr)

    stop = time.time()
    
    time1 = stop-start
    
    
    start = time.time()
    for j in range(10000):
        insertion_sort(arr)

    stop = time.time()
    
    time2 = stop-start
    
    
    if time2 > time1:
        size = i+1
        break
    


print(size)

   
            
    



