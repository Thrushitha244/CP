import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
def max_crossing_sum(arr, left, mid, right):
    total = 0
    left_sum = -10**18
    for i in range(mid, left - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)
    total = 0
    right_sum = -10**18
    for i in range(mid + 1, right + 1):
        total += arr[i]
        right_sum = max(right_sum, total)
    return left_sum + right_sum
def max_subarray(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    left_max = max_subarray(arr, left, mid)
    right_max = max_subarray(arr, mid + 1, right)
    cross_max = max_crossing_sum(arr, left, mid, right)

    return max(left_max, right_max, cross_max)
T = int(input().strip())
results = []
for _ in range(T):
    N = int(input().strip())
    arr = list(map(int, input().split()))
    results.append(str(max_subarray(arr, 0, N - 1)))
print("\n".join(results))