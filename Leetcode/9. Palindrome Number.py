def isPalindrome(x: int) -> bool:
    
    x = str(x)
    lenn = len(x)
    
    for i in range(lenn//2):
        if  x[i] != x[lenn-i-1]:
            return False
    return True
    
    
    
    
num = 1
print(isPalindrome(num))

