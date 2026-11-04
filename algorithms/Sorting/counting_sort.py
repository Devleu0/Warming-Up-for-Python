"""Counting sort: 0 이상의 정수, 값의 범위가 작을 때 O(N + K)."""


def counting_sort(data):
    """정렬된 새 리스트를 반환한다. 음수는 지원하지 않는다."""
    if not data:
        return []
    if min(data) < 0:
        raise ValueError("counting_sort supports non-negative integers only")
    count = [0] * (max(data) + 1)
    for value in data:
        count[value] += 1
    result = []
    for value, freq in enumerate(count):
        result.extend([value] * freq)
    return result


if __name__ == "__main__":
    print(counting_sort([8, 5, 4, 7, 2]))  # [2, 4, 5, 7, 8]
