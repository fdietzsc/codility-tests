def solution(A):
    if not A:
        return 0
    A = sorted(A)
    counter = 0
    prev_val = 1000001
    for val in A:
        if val == prev_val:
            continue
        else:
            counter += 1
            prev_val = val
    return counter

test_data = ([2, 1, 1, 2, 3, 1],
             [],
             [1],
             [1, 2, 3])

expected = (3, 0, 1, 3)

for data, expected in zip(test_data, expected):
    try:
        res = solution(data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
