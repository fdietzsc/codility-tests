def solution(A):
    profit = 0
    gain = 0
    for i in range(0, len(A) - 1):
        # keep track of incremental gain
        gain = max(0, gain + A[i + 1] - A[i])
        # keep track of overall max profit
        profit = max(profit, gain)

    return profit

test_data = ([23171, 21011, 21123, 21366, 21013, 21367],
             [],
             )

expected = (356, 0)

for data, expected in zip(test_data, expected):
    try:
        res = solution(data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
