def solution(A, B, K):
    if K == 1:
        return B - A + 1

    if A == B:
        if A == 0 or A % K == 0:
            return 1
        else:
            return 0

    counter = 0
    if B // 2 < K <= B:
        counter += 1
    elif K <= B // 2:
        counter += B//K - A//K

    if A % K == 0:
        counter += 1

    return counter

test_data = ((3, 13, 3),
             (6, 11, 2),
             (1, 12, 5),
             (0, 0, 3),
             (0, 0, 1),
             (2, 12, 1),
             (5, 5, 2),
             (6, 11, 100),
             (0, 14, 2),
             (2, 12, 2),
             (0, 2, 1),
             (0, 2, 3),
             (5, 5, 5),
             (6, 6, 3),
             (11, 13, 2),
             (11, 345, 17),
             ([0, 2000000000, 2000000000])
             )

expected = (4, 3, 2, 1, 1, 11, 0, 0, 8, 6, 3, 1, 1, 1, 1, 20, 2)

for data, expected in zip(test_data, expected):
    try:
        res = solution(*data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
