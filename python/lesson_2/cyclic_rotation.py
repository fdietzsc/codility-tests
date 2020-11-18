def solution(A, K):
    if A:
        if K <= len(A):
            shift = K
        else:
            shift = K%len(A)
        return A[-shift:] + A[:-shift]
    else:
        return []

# test data
test_data = (([3, 8, 9, 7, 6], 3),
             ([0, 0, 0], 1),
             ([1, 2, 3, 4], 4),
             ([], 10),
             ([1, 1, 2, 3, 5], 42))

expected = ([9, 7, 6, 3, 8],
            [0, 0, 0],
            [1, 2, 3, 4],
            [],
            [3, 5, 1, 1, 2])

