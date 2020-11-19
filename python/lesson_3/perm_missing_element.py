def solution(A):
    if not A:
        return 1
    if len(A) == 1:
        return 2 if A[0] == 1 else 1
    A = sorted(A)
    if A[0] > 1:
        return 1
    for i, val in enumerate(A[:-1]):
        if A[i+1] - val != 1:
            return val + 1
    return A[-1] + 1


test_data = ([],
             [1],
             [2],
             [2, 1],
             [3, 2],
             [2, 1, 3],
             [2, 4, 3],
             [2, 3, 1, 5],
             [0, 2, 8, 3, 7, 4, 6, 5])

expected = (1, 2, 1, 3, 1, 4, 1, 4, 1)

for data, expected in zip(test_data, expected):
    try:
        res = solution(data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
