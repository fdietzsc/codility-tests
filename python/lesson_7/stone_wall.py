def solution(H):
    N = len(H)
    if N == 1:
        return 1

    blocks = [H[0]]
    foundation = [0]
    # O(N)
    for h in range(1, N):
        height = H[h]
        if height == H[h - 1]:
            continue
        if height < H[h - 1]:
            delta = H[h - 1] - height
            # check if there is one stone that
            # can serve as foundation for current one.
            # i.e. pop foundation until we find one
            while foundation:
                d = foundation.pop()
                # decrement last foundation and add
                # new stone later
                if d > delta:
                    foundation.append(d - delta)
                    break
                else:
                    delta -= d
                if delta == 0:
                    break
            if delta != 0:
                blocks.append(H[h])
        else:
            # if direction is upwards
            # always a new block is required
            foundation.append(height - H[h - 1])
            blocks.append(H[h])

    return len(blocks)


test_data = ([8, 8, 5, 7, 9, 8, 7, 4, 8],
             [8, 8, 5, 7, 9, 8, 7, 5, 8],
             [8, 8, 5, 5, 5, 5, 5, 4, 4],
             [3, 1, 3],
             [1, 1],
             [2, 1],
             [1, 2],
             [2, 5, 1, 4, 6, 7, 9, 10, 1]
             )

expected = (7, 6, 3, 3, 1, 2, 2, 8)

for data, expected in zip(test_data, expected):
    try:
        res = solution(data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')

