def check(n): # 222
    while n != 0: 
        d = n % 10 # 3
        if d%2 != 1: # 3%2 != 1
            return False
        n = n // 10
    return True

print(check(13579))

