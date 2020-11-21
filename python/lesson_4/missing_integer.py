def solution(A):

    X = len(A)

    if X == 1 and A[0] != 1:
        return 1

    bin = X*[False]
    for i in range(0, X):
        if A[i] < 0:
            continue
        if A[i] > X:
            continue

        bin[A[i] - 1] = True

    for i, val in enumerate(bin):
        if not val:
            return i + 1

    return X + 1


test_data = ([1, 3, 6, 4, 1, 2],
             [1, 2, 3],
             [-1, -3],
             [-3, 1],
             [-3, 2],
             [-3, 5],
             [-100, 1, 4, 5],
             [1, 2, -100, 5],
             [0],
             [1],
             [2],
             [3])

expected = (5, 4, 1, 2, 1, 1, 2, 3, 1, 2, 1, 1)

for data, expected in zip(test_data, expected):
    try:
        res = solution(data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
