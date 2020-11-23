def solution(A):
    if len(A) < 3:
        return 0
    A = sorted(A)
    for i in range(0, len(A) - 2):
        p = A[i]
        q = A[i + 1]
        r = A[i + 2]
        if p + q > r and q + r > p and r + p > q:
            return 1

    return 0

test_data = ([10, 2, 5, 1, 8, 20],
             [10, 50, 5, 1],
             [5, 8, 10],
             [10, 50, 1],
             [])

expected = (1, 0, 1, 0, 0)

for data, expected in zip(test_data, expected):
    try:
        res = solution(data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
