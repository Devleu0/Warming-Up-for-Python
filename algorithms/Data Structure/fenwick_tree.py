import sys

# Fenwick Tree (Binary Indexed Tree) 클래스
class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, i, diff):
        """i번째 인덱스에 diff를 더함"""
        while i < len(self.tree):
            self.tree[i] += diff
            i += (i & -i)

    def query(self, i):
        """1부터 i까지의 합을 반환"""
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)
        return res

def get_inversion_count(arr):
    n = len(arr)
    
    # 1. 좌표 압축 수행
    # 1등부터 N등까지의 순위로 변환. (1-based index 사용 위해 +1)
    sorted_unique = sorted(list(set(arr)))
    rank_map = {val: i+1 for i, val in enumerate(sorted_unique)}
    compressed = [rank_map[x] for x in arr]
    
    # 2. 펜윅 트리를 이용한 역전수 계산
    # 트리의 크기는 압축된 값의 최대값(종류의 개수) 만큼이면 충분
    max_rank = len(sorted_unique)
    bit = FenwickTree(max_rank)
    
    inversion_count = 0
    
    # 배열을 왼쪽부터 순회
    for i in range(n):
        current_rank = compressed[i]
        
        # query(max_rank): 현재까지 나온 수 전체 개수
        # query(current_rank): 현재 나온 수 중, '나보다 작거나 같은' 수의 개수
        # 따라서 (전체 - 작거나 같은) = '나보다 큰 수의 개수' (이미 이전에 등장한)
        bigger_exist = bit.query(max_rank) - bit.query(current_rank)
        
        inversion_count += bigger_exist
        
        # 현재 수를 트리에 등록
        bit.update(current_rank, 1)
        
    return inversion_count

if __name__ == "__main__":
    # 예제 입력
    # (i, j) 쌍 중 i < j 이면서 A[i] > A[j] 인 것
    # (5, 1), (5, 2), (3, 1), (3, 2), (4, 1), (4, 2) => 총 6개 예상
    data = [5, 3, 1, 4, 2]
    
    print(f"입력 배열: {data}")
    result = get_inversion_count(data)
    print(f"역전수(Inversion Count): {result}")
    
    assert result == 6
