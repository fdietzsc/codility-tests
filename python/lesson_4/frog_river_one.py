def solution(X, A):

    # Delivers correct results but fails some performance tests
    # bin = X*[False]
    # for i in range(0, len(A)):
    #     bin[A[i] - 1] = True
    #     if all(bin):
    #         return i
    # # can never jump
    # return -1

    # a little more elegant version that also passes
    # all tests :-)
    bin = X*[True]
    cumsum = X * (X + 1) // 2
    for i in range(0, len(A)):
        if bin[A[i] - 1]:
            cumsum -= A[i]
            bin[A[i] - 1] = False

        if cumsum == 0:
            return i
    # can never jump
    return -1


test_data = ((5, [1, 3, 1, 4, 2, 3, 5, 4]),
             (5, [1, 3, 1, 4, 2, 3, 5]),
             (5, [5, 3, 1, 4, 2, 1, 5, 5]),
             (5, [5, 5, 1, 4, 2, 1, 5, 3]),
             (2, [1, 1]))

expected = (6, 6, 4, 7, -1)

for data, expected in zip(test_data, expected):
    try:
        res = solution(*data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
