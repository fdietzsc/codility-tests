def solution(N):
    b_rep = '{:b}'.format(N)
    counter = 0
    res = 0
    prev_val = 0
    count = False
    for val in b_rep:
        val = int(val)
        if val - prev_val == -1:
            count = True
            counter += 1
        if val - prev_val == 0 and count:
            counter += 1
        if val - prev_val == 1:
            count = False
            res = max(res, counter)
            counter = 0
        prev_val = val
    return res
