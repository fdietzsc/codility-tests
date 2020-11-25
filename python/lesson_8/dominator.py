def solution(A):
    if not A:
        return -1
    if len(A) == 1:
        return 0

    # find possible candidates by pairwise comparing
    # and stacking
    candidates = [A[0]]
    for i in range(1, len(A)):
        if candidates:
            if A[i] != candidates[-1]:
                candidates.pop()
            else:
                candidates.append(A[i])
        else:
            candidates.append(A[i])

    # remove duplicates
    candidates = list(set(candidates))
    leader_pos = -1
    while candidates:
        candidate = candidates.pop()
        counter = 0
        for i, val in enumerate(A):
            if val == candidate:
                counter += 1
                leader_pos = i
        if counter > len(A) // 2:
            return leader_pos

    return -1


test_data = ([3, 4, 3, 2, 3, -1, 3, 3],
             [],
             [1],
             [1, 1, 1],
             [6, 8, 4, 6, 8, 6, 6]
             )

expected = (7, -1, 0, 2, 6)

for data, expected in zip(test_data, expected):
    try:
        res = solution(data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'test failed for {data}: {res} != {expected}')

