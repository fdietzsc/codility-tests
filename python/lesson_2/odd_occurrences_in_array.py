def solution(A):
    if len(A) == 1:
        return A[0]
    A = sorted(A)
    for i, pair in enumerate(zip(A[:-1:2], A[1::2])):
        next_block = A[2 * (i + 1)]
        if pair[0] != pair[1]:
            res = pair[0]
            break
        else:
            res = next_block
    return res


test_data = ([5, 3, 6, 6, 3, 7, 5],
             [9, 3, 9, 3, 9, 7, 9],
             [3, 3, 3, 42, 3, 3, 3],
             [3, 3, 3, 3, 3, 3, 9],
             [3, 9, 9, 9, 9, 9, 9],
             [1, 3, 1],
             [42],
             [5, 2, 2, 3, 3, 4, 5],
             [2, 2, 3, 3, 4],
             [2, 3, 2, 3, 4])

expected = (7, 7, 42, 9, 3, 3, 42, 4, 4, 4)


for data, expected in zip(test_data, expected):
    try:
        res = solution(data.copy())
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
