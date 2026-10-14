def double_binary_search(a = [], b = []):
    # O(min(M, N) * log(2 * max(M, N) / min(M, N)))

    if len(a) > len(b):
        a, b = b, a

    def search(la, ra, lb, rb):
        if la > ra or lb > rb:
            return False

        target = a[(la + ra) // 2]

        l, r = lb - 1, rb + 1
        while (r - l > 1):
            m = (l + r) // 2
            if (b[m] == target):
                return True
            elif (b[m] > target):
                r = m
            else:
                l = m

        return search(la, (la + ra) // 2 - 1, lb, l) or search((la + ra) // 2 + 1, ra, r, rb)

    return search(0, len(a) - 1, 0, len(b) - 1)