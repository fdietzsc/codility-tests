def solution(A):

    X = len(A)
    bin = X*[True]
    termial = X * (X + 1) // 2
    for i in range(0, len(A)):
        if A[i] > X:
            return 0
        if bin[A[i] - 1]:
            termial -= A[i]
            bin[A[i] - 1] = False

    if termial == 0:
        return 1
    else:
        return 0

test_data = ([4, 1, 3, 2],
             [4, 1, 3],
             [1],
             [2])

expected = (1, 0, 1, 0)

for data, expected in zip(test_data, expected):
    try:
        res = solution(data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
