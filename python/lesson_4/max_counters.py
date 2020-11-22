def solution(N, A):
    counters = [0]*N
    max_counter = 0
    max_val = 0

    for i in range(0, len(A)):
        if A[i] <= N:
            # revisited elements are set to global (current) max
            # if not already done.
            counters[A[i]-1] = max(max_val, counters[A[i]-1])
            counters[A[i]-1] += 1
            max_counter = max(max_counter, counters[A[i]-1])

        # set new global max
        if A[i] == N+1:
            max_val = max_counter

    # all elements that have not been revisited are now set to
    # global max
    for i, val in enumerate(counters):
        counters[i] = max(max_val, val)

    return counters


test_data = ((5, [3, 4, 4, 6, 1, 4, 4]),
             (3, [1]),
             (3, [5]),
             (4, [3, 4, 4, 5]),
             (4, [5, 5, 5, 5]),
             (5, [4, 6, 4, 6, 4, 4, 6, 4, 6, 4, 6]))

expected = ([3, 2, 2, 4, 2],
            [1, 0, 0],
            [0, 0, 0],
            [2, 2, 2, 2],
            [0, 0, 0, 0],
            [6, 6, 6, 6, 6])

for data, expected in zip(test_data, expected):
    try:
        res = solution(*data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
