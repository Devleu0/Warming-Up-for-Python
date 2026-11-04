import sys
from bisect import bisect_left

def coordinate_compression_basic(arr):
    """
    기본적인 좌표 압축 구현 (Dictionary 활용)
    Time Complexity: O(N log N)
    """
    # 1. 중복 제거 및 정렬
    sorted_unique = sorted(list(set(arr)))
    
    # 2. 값 -> 압축된 인덱스 매핑 생성 (Dictionary)
    compression_map = {value: index for index, value in enumerate(sorted_unique)}
    
    # 3. 원본 배열 변환
    compressed_arr = [compression_map[x] for x in arr]
    
    return compressed_arr, compression_map

def coordinate_compression_bisect(arr):
    """
    bisect 활용 구현 (C++ lower_bound 스타일)
    """
    sorted_unique = sorted(list(set(arr)))
    
    # bisect_left를 사용하여 해당 값이 정렬된 배열에서 몇 번째 인덱스인지 찾음
    compressed_arr = [bisect_left(sorted_unique, x) for x in arr]
    
    return compressed_arr

if __name__ == "__main__":
    # 값의 격차는 크지만 개수는 적음
    data = [2492, 10, 99999999, 10, -500, 2492]
    
    print(f"원본 데이터: {data}")
    
    # 방법 1
    compressed, mapping = coordinate_compression_basic(data)
    print(f"\n[Dictionary 방식]")
    print(f"압축된 결과: {compressed}")
    print(f"매핑 정보(Val->Idx): {mapping}")
    
    # 방법 2
    compressed_bi = coordinate_compression_bisect(data)
    print(f"\n[Bisect 방식]")
    print(f"압축된 결과: {compressed_bi}")
    
    # 0부터 시작하는 순위로 잘 변환되었는지 확인
    # -500 -> 0, 10 -> 1, 2492 -> 2, 99999999 -> 3
    assert compressed_bi == [2, 1, 3, 1, 0, 2]
    print("\n 좌표 압축 정상 동작 확인")
