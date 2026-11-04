''' Fenwick Tree (Binary Indexed Tree)
- 점 갱신 / 구간 합: 둘 다 O(logN)
- 인덱스는 1부터 사용
'''


class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (size + 1)

    def update(self, i, diff):
        """i번째 값에 diff를 더함"""
        while i <= self.n:
            self.tree[i] += diff
            i += (i & -i)

    def query(self, i):
        """1부터 i까지의 합"""
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)
        return res

    def interval_sum(self, start, end):
        """start부터 end까지의 합"""
        return self.query(end) - self.query(start - 1)

    def set(self, i, value):
        """i번째 값을 value로 바꿈"""
        self.update(i, value - self.interval_sum(i, i))


# ---------------------------------------------------------------
# 예제 1: 기본 구간 합 (값 변경이 섞인 구간 합 쿼리)
# ---------------------------------------------------------------
def interval_sum_demo():
    bit = FenwickTree(5)
    for i, v in enumerate([1, 2, 3, 4, 5], 1):
        bit.set(i, v)

    print(bit.interval_sum(2, 5))   # 14
    bit.update(3, -2)               # 3번째 값 3 -> 1
    print(bit.interval_sum(2, 5))   # 12
    bit.update(5, 2)                # 5번째 값 5 -> 7
    print(bit.interval_sum(2, 5))   # 14
    print(bit.interval_sum(1, 5))   # 15


# ---------------------------------------------------------------
# 예제 2: 역전수(Inversion Count) — 좌표 압축 + 펜윅 트리
# (i, j) 쌍 중 i < j 이면서 A[i] > A[j] 인 것의 개수
# ---------------------------------------------------------------
def get_inversion_count(arr):
    # 1. 좌표 압축: 값을 1..K 순위로 변환 (1-based)
    sorted_unique = sorted(set(arr))
    rank_map = {val: i + 1 for i, val in enumerate(sorted_unique)}
    compressed = [rank_map[x] for x in arr]

    # 2. 왼쪽부터 보면서 "이미 나온 수 중 나보다 큰 수"를 센다
    max_rank = len(sorted_unique)
    bit = FenwickTree(max_rank)
    inversion_count = 0
    for current_rank in compressed:
        # 전체 개수 - (나보다 작거나 같은 수의 개수) = 나보다 큰 수의 개수
        inversion_count += bit.query(max_rank) - bit.query(current_rank)
        bit.update(current_rank, 1)
    return inversion_count


if __name__ == "__main__":
    interval_sum_demo()

    data = [5, 3, 1, 4, 2]
    result = get_inversion_count(data)
    print(f"입력 배열: {data}, 역전수: {result}")
    assert result == 7   # (5,3) (5,1) (5,4) (5,2) (3,1) (3,2) (4,2)
