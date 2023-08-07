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
def selection_sort(ls:list) -> list:
    
    len_list = len(ls)
    
    while len_list != 1:
        
        max_index = 0
        for i in range(len_list):
           if  ls[i] >= ls[max_index]:
               
               max_index = i
               
        ls[max_index],ls[len_list-1] = ls[len_list-1],ls[max_index]  
            
            
        len_list -= 1
        
    return ls



ls = [5,3,2,6,1,4]

print(selection_sort(ls))
    