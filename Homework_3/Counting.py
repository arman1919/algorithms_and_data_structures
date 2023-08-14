def counting_sort(arr):
    if len(arr) == 0:
        return []

    max_value = max(arr) 
    min_value = min(arr)  
    count_range = max_value - min_value + 1 

    count = [0] * count_range  

  
    for num in arr:
        count[num - min_value] += 1   

    sorted_arr = []
    print(count)
    for i in range(count_range):
        sorted_arr.extend([i + min_value] * count[i])

    return sorted_arr


input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = counting_sort(input_array)
print(sorted_array)


