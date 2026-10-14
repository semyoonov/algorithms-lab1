def two_pointers(a = [], b = []):
    # O(M + N)

    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            return True
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    
    return False