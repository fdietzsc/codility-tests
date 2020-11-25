def solution(A):
    if not A:
        return 0
    max_slice = 0
    max_sum = 0
    max_val = -3000000000
    for val in A:
        max_sum = max(0, max_sum + val)
        max_slice = max(max_slice, max_sum)
        # keep track of max value of A
        max_val = max(max_val, val)

    if max_slice == 0:
        return max_val
    else:
        return max_slice


test_data = ([3, 2, -6, 4, 0],
             [],
             [-10],
             [-2, -2],
             [-2, -2, 0],
             [-10, -2, 2, 10],
             [-200000, -7, -6, -5, -4, -3, -2, -1],
             [-200000, -1, -2, -3, -4, -5, -6, -7],
             )

expected = (5, 0, -10, -2, 0, 12, -1)

for data, expected in zip(test_data, expected):
    try:
        res = solution(data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
