def bucket_sort(arr, num_buckets):
    if len(arr) == 0:
        return arr

    min_value = min(arr)
    max_value = max(arr)
    bucket_range = (max_value - min_value) / num_buckets

   
    buckets = [[] for _ in range(num_buckets)]

   
    for num in arr:
        index = int((num - min_value) / bucket_range)
        if index >= num_buckets:
            index = num_buckets - 1
        buckets[index].append(num)

   
    for i in range(num_buckets):
        buckets[i].sort()

    
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array


input_array = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
num_buckets = 5
sorted_array = bucket_sort(input_array, num_buckets)
print(sorted_array)
