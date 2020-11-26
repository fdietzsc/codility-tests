def solution(N):
    i = 1
    result = 0
    while i * i < N:
        if N % i == 0:
            # if i is a divisor then N/i is also one
            result += 2
        i += 1

    if i * i == N:
        result += 1

    return result

test_data = (24,
             )

expected = (8,)

for data, expected in zip(test_data, expected):
    try:
        res = solution(data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
