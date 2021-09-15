#  1~n 합
def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n - 1) + n


# a~b 합
def sum_ab(a, b):
    if a > b:
        return 0
    elif a == b:
        return a
    else:
        m = (a + b) // 2
        return sum_ab(a, m) + sum_ab(m + 1, b)


# 1~n 곱
def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


# find max_value of list A
def find_max(A, n):
    if len(A) == 1:
        return A[0]
    if A[0] >= find_max(A[1 : n + 1], n - 1):
        return A[0]
    else:
        return find_max(A[1 : n + 1], n - 1)


# find max_value of list A with max()
def _find_max(A, n):
    if len(A) == 1:
        return A[0]
    else:
        return max(_find_max(A[1:n], n - 1), A[0])


# A 리스트 거꾸로 배치
def reverse_list(A):
    if len(A) == 1:
        return A
    else:
        return reverse_list(A[1:]) + A[:1]


# A[start]~A[end-1] 거꾸로 배치
def _reverse_list(A, start, end):
    if start < end - 1:
        A[start], A[end - 1] = A[end - 1], A[start]
        _reverse_list(A, start + 1, end - 1)
    return A


# {0, 1, ... , n-1} 의 모든 부분집합 출력

# 길이가 n인 순열 모두 출력
