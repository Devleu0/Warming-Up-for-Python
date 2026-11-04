"""Quick sort 와 Quick select 구현 모음."""
import random


def quick_sort_inplace(data, start=0, end=None):
    """제자리(in-place) 퀵 정렬. 첫 원소를 pivot 으로 사용한다."""
    if end is None:
        end = len(data) - 1
    if start >= end:
        return data
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and data[left] <= data[pivot]:
            left += 1
        while right > start and data[right] >= data[pivot]:
            right -= 1
        if left > right:
            data[right], data[pivot] = data[pivot], data[right]
        else:
            data[left], data[right] = data[right], data[left]
    quick_sort_inplace(data, start, right - 1)
    quick_sort_inplace(data, right + 1, end)
    return data


def quick_sort(arr):
    """파이썬스러운 퀵 정렬. 새 리스트를 반환한다."""
    if len(arr) <= 1:
        return list(arr)
    pivot = random.choice(arr)
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]  # 중복 고려
    return quick_sort(lows) + pivots + quick_sort(highs)


def quick_select(arr, k):
    """arr 에서 k 번째(1부터 시작)로 작은 값을 반환한다."""
    if not 1 <= k <= len(arr):
        raise ValueError("k must satisfy 1 <= k <= len(arr)")
    pivot = random.choice(arr)
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]
    if k <= len(lows):
        return quick_select(lows, k)
    if k <= len(lows) + len(pivots):
        return pivots[0]
    return quick_select(highs, k - len(lows) - len(pivots))


if __name__ == "__main__":
    print(quick_sort_inplace([8, 5, 4, 7, 2]))  # [2, 4, 5, 7, 8]
    sample = [5, 3, 2, 4, 1]
    print(quick_select(sample, 3))  # 3
    print(quick_sort(sample))  # [1, 2, 3, 4, 5]
