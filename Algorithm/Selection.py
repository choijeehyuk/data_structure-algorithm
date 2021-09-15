# MAX_VALUE of list A
def MAX_list(A):
    current = A[0]
    for i in A:
        if current < i:
            current = i
    return current


# MAX_VALUE, MIN_VALUE of list A
def MAXMIN_list(A):
    current_max = A[0]
    current_min = A[0]
    for i in A[0:]:
        if current_max < i:
            current_max = i
        if current_min > i:
            current_min = i
    return current_min, current_max


# 리스트 A에서 k 번째로 작은 수
def quick_select(L, k):
    p = L[0]
    A, B, M = [], [], []
    for i in L:
        if p > i:
            A.append(i)
        elif p < i:
            B.append(i)
        else:
            M.append(i)

    if len(A) >= k:
        return quick_select(A, k)
    elif len(A) + len(M) < k:
        return quick_select(B, k - len(A) - len(M))
    else:
        return M[0]


print(quick_select([15, 23, 22, 14, 12, 1, 2], 7))
