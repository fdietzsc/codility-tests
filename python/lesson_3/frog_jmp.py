def solution(X, Y, D):
    if X == Y:
        return 0
    if X+D >= Y:
        return 1
    distance = Y-X
    if distance % D != 0:
        return distance // D + 1
    else:
        return distance // D

test_data = ((10, 85, 30),
             (10, 25, 1),
             (1, 1, 1),
             (1, 2, 1),
             (1, 5, 4),
             (1, 5, 2),
             (1, 5, 5),
             (1, 5, 3),
             (4, 20, 5))

expected = (3, 15, 0, 1, 1, 2, 1, 2, 4)

for data, expected in zip(test_data, expected):
    try:
        res = solution(*data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
