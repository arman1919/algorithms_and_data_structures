import time

def time_calculation(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Function execution time {func.__name__}: {execution_time:.6f} seconds")
        return result
    return wrapper


@time_calculation
def  insertion_sort(ls:list) -> list:
    
    len_list = len(ls)
    for i in range(1, len_list):
        key = ls[i]
        j = i - 1
       
        while j >= 0 and key < ls[j]:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
    
    return ls




ls = [3,5,1,6,4,2]

print(insertion_sort(ls))