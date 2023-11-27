def pairs(k, arr):
    return sum((a - b) == k for a in arr for b in arr)
