def radix_sort(arr):
    if len(arr) == 0:
        return arr

    
    max_num = max(arr)
    num_digits = len(str(max_num))

   
    for digit in range(num_digits):
        arr = counting_sort_by_digit(arr, digit)

    return arr

def counting_sort_by_digit(arr, digit):
    count = [0] * 10
    output = [0] * len(arr)

    for num in arr:
        count[(num // 10**digit) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = len(arr) - 1
    while i >= 0:
        output[count[(arr[i] // 10**digit) % 10] - 1] = arr[i]
        count[(arr[i] // 10**digit) % 10] -= 1
        i -= 1

    return output


input_array = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_array = radix_sort(input_array)
print(sorted_array)
    