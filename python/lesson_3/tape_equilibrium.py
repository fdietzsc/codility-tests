def solution(A):
    res = 1000000000
    # passes correctness test but is very slow
    # O(N*N)
    # counter = 0
    # for i in range(0, len(A[:-1])):
    #     counter += A[i]
    #     diff = abs(counter - sum(A[i+1:]))
    #     res = min(diff, res)
    # return res

    # this is a better solution as it is only of
    # O(N)
    dis = len(A) // 2
    odd = len(A)%2 != 0
    forward = []
    backward = []
    fwd_counter = 0
    bwd_counter = 0
    for i in range(0, dis):
        fwd_counter += A[i]
        forward.append(fwd_counter)
        bwd_counter += A[-1 - i]
        backward.append(bwd_counter)

    s = backward[-1] + forward[-1]
    if odd:
        s += A[dis]
    for i in range(0, dis):
        res = min(abs(s - 2*forward[i]), abs(s - 2*backward[i]), res)

    return res


test_data = ([3, 1, 2, 4, 3],
             [4, 1],
             [0, 1, 2],
             [1, 1, 2],
             [1, 2, 3],
             [3, 3, 3, 3])

expected = (1, 3, 1, 0, 0, 0)

for data, expected in zip(test_data, expected):
    try:
        res = solution(data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
