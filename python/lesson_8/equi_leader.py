def solution(A):
    if len(A) == 1:
        return 0

    candidates = [A[0]]
    for i in range(1, len(A)):
        if candidates:
            if A[i] != candidates[-1]:
                candidates.pop()
            else:
                candidates.append(A[i])
        else:
            candidates.append(A[i])

    if not candidates:
        return 0

    candidates = list(set(candidates))
    while candidates:
        candidate = candidates.pop()
        counter = 0
        leader_loc = []
        for i, val in enumerate(A):
            if val == candidate:
                counter += 1
                leader_loc.append(i)
        if counter > len(A) // 2:
            break
        else:
            return 0

    counter = 0
    left_leaders = 0
    leader_loc = leader_loc[::-1]
    for i in range(len(A)):
        if not leader_loc:
            break
        if i == leader_loc[-1]:
            left_leaders += 1
            leader_loc.pop()
        left_non_leaders = i - left_leaders + 1
        right_leaders = len(leader_loc)
        right_non_leaders = len(A) - left_non_leaders - left_leaders - right_leaders
        if left_leaders > left_non_leaders and right_leaders > right_non_leaders:
            counter += 1

    return counter

test_data = ([4, 3, 4, 4, 4, 2],
             [4, 3, 4, 3, 4, 2],
             [4, 4, 2, 5, 3, 4, 4, 4]
             )

expected = (2, 0, 3)

for data, expected in zip(test_data, expected):
    try:
        res = solution(data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'test failed for {data}: {res} != {expected}')

