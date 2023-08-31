def hash_integer(n, table_size):
    A = (5 ** 0.5 - 1) / 2  
    result = n * A
    result -= int(result)  
    result *= table_size
    return int(result)




