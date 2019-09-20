import math

# There are many ways to solve this, but there are 2 ways to solve in O(n) time and O(1) space


# solution using sum
def two_missing(arr):
    n = len(arr) + 2
    total_sum = sum(range(1, n+1))
    arr_sum = sum(arr)
    missing_total = total_sum - arr_sum
    pivot = missing_total // 2

    total_left_sum = sum(range(1, pivot+1))
    total_right_sum = sum(range(pivot+1, n+1))
    arr_left_sum = sum(x for x in arr if x <= pivot)
    arr_right_sum = sum(x for x in arr if x > pivot)

    return total_left_sum - arr_left_sum, total_right_sum - arr_right_sum


def quadratic(a, b, c):
    s1 = (-b + math.sqrt((b**2 - 4*a*c))) / (2 * a)
    s2 = (-b - math.sqrt((b**2 - 4*a*c))) / (2 * a)
    return int(s1), int(s2)


def two_missing_math(arr):
    n = len(arr) + 2
    total_sum = sum(range(1, n+1))
    total_sum_of_squared = sum(i**2 for i in range(1, n+1))
    arr_sum = sum(arr)
    arr_sum_of_squared = sum(i**2 for i in arr)
    a = total_sum - arr_sum
    b = total_sum_of_squared - arr_sum_of_squared

    j1, j2 = quadratic(2, -(2*a), a**2-b)
    if 1 <= j1 <= n:
        return a-j1, j1
    elif 1 <= j2 <= n:
        return a-j2, j2


if __name__ == '__main__':
    a = [4, 2, 3]
    result = two_missing_math(a)
    assert result == (1, 5)

    a = [5, 1, 2, 6]
    result = two_missing_math(a)
    assert result == (3,4)
