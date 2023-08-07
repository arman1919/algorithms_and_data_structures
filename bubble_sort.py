import time

# bubble sort in Python

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
def bubble_sort(ls:list)-> list:
    
    len_list = len(ls)
    
    while len_list != 1:
       
        new_list = ls.copy()
        for i in range(len_list-1):
            
            
            if ls[i] >= ls[i+1]:
                ls[i],ls[i+1] = ls[i+1],ls[i]
                
        if ls == new_list: # if there was no replacement of elements, then the list is already sorted
            
            break
        
        len_list -= 1
    return ls
    


ls = [1,2,4,3,5,6]

print(bubble_sort(ls))
