def solution(N):
    i = 1
    perimeter = 2*(N + 1)
    while i * i < N:
        if N % i == 0:
            perimeter = min(perimeter, 2 * (i + N//i))
        i += 1

    if i * i == N:
        perimeter = min(perimeter, 2 * (i + N // i))

    return perimeter

test_data = (30, 1, 36, 101)

expected = (22, 4, 24, 204)

for data, expected in zip(test_data, expected):
    try:
        res = solution(data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
