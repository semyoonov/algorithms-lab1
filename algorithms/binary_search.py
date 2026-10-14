def binary_search(a = [], b = []):
    # O(min(M, N) * log(max(M, N)))

    if len(a) > len(b):
        a, b = b, a

    for i in a:
        l = 0
        r = len(b) - 1

        while r - l > 1:
            m = (l + r) // 2
            if b[m] < i:
                l = m
            else:
                r = m
        
        if b[l] == i or b[r] == i:
            return True
    
    return False