def solution(S):
    if len(S) == 1:
        return 0
    opened = []
    opening = {')': '(', ']': '[', '}': '{'}
    for s in S:
        if s in ['(', '{', '[']:
            opened.append(s)
        else:
            if not opened or opening[s] != opened.pop():
                return 0
    return 0 if opened else 1


test_data = ('{[()()]}',
             '([)()]',
             '',
             '[',
             ']]]]',
             '[[[['
             )

expected = (1, 0, 1, 0, 0, 0)

for data, expected in zip(test_data, expected):
    try:
        res = solution(data)
        assert res == expected
    except AssertionError:
        raise AssertionError(f'Test failed for {data}: {res} != {expected}')
