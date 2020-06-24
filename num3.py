def get_zeros(n):
    res = 0
    # count zeros for all factorials before n
    # return zeros only for n
    for i in range(n+1):
        res = i//5 + (i - (i % 25))//25
    return res
