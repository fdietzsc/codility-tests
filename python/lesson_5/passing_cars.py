def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


def count(P, x, y):
    return P[y + 1] - P[x]


def solution(A):
    sums = prefix_sums(A)
    counter = 0
    for i in range(0, len(A)):
        if A[i] == 0:
            counter += count(sums, i, len(A) - 1)

    if counter <= 1000000000:
        return counter
    else:
        return -1


test_data = ([0, 1, 0, 1, 1],)

expected = (5,)

for data, expected in zip(test_data, expected):
    try:
        res = solution(data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
