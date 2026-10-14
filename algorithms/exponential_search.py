def exponential_search(a = [], b = []):
    # O(min(M, N) * log(2 * max(M, N) / min(M, N)))

    if len(a) > len(b):
        a, b = b, a
    
    j = 0
    n = len(b)

    for u in a:
        if j >= n:
            break
        if b[j] == u:
            return True
        elif b[j] > u:
            continue
        
        step = 1
        while j + step < n and b[j + step] < u:
            step *= 2
        
        l = j + step // 2 - 1
        r = min(j + step, n - 1) + 1

        while (r - l > 1):
            m = (l + r) // 2
            if b[m] == u:
                return True
            elif b[m] > u:
                r = m
            else:
                l = m
        j = r

    return False