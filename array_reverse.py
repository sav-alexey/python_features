def solution(A):
    # A.reverse()
    N = len(A)
    for i in range(N//2):
        k = N - i - 1
        A[i], A[k] = A[k], A[i]
    return A