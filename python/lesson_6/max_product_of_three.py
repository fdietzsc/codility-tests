def solution(A):
    A = sorted(A)
    smallest = A[0:3]
    largest = A[-1:-4:-1]
    res = max(largest[0] * largest[1] * largest[2],
              smallest[0] * smallest[1] * largest[0])

    return res

test_data = ([-3, 1, 2, -2, 5, 6],
             [-3, 1, 2, -2, -5, -6])

expected = (60, 60)

for data, expected in zip(test_data, expected):
    try:
        res = solution(data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
