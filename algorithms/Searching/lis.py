import sys
from bisect import bisect_left

# LIS (Longest Increasing Subsequence)
def lis_nlogn(nums):
    """
    최장 증가 부분 수열 (LIS) - O(N log N)
    :param nums: 입력 수열
    :return: LIS의 길이
    """
    if not nums:
        return 0
    
    # tails[i] = 길이가 i+1인 증가 부분 수열 중, '마지막 원소'의 최소값
    # tails는 항상 오름차순으로 정렬된 상태를 유지함 -> 이분 탐색 가능
    tails = []
    
    for x in nums:
        # tails 배열에서 x가 들어갈 수 있는 위치(x보다 크거나 같은 첫 번째 위치) 찾기
        idx = bisect_left(tails, x)
        
        # x가 현재 만든 모든 LIS의 마지막 값보다 크다면 -> LIS 길이 연장 가능
        if idx == len(tails):
            tails.append(x)
        # 아니라면 -> 기존 길이의 LIS 마지막 값을 더 작은 x로 갱신 (미래를 위해 유리함)
        else:
            tails[idx] = x
            
    # tails의 길이가 LIS의 길이
    # 주의: tails 배열 자체가 실제 LIS 수열을 의미하지는 않음 (길이와 끝 값 정보만 유효)
    return len(tails)

if __name__ == "__main__":
    # 예제 데이터
    # LIS: [1, 2, 3, 5] 또는 [1, 2, 4, 5] -> 길이 4
    data = [10, 9, 2, 5, 3, 7, 101, 18]
    
    print(f"입력 수열: {data}")
    result = lis_nlogn(data)
    print(f"LIS 길이: {result}") # 예상: 4 ([2, 3, 7, 18] 등)
    
    assert result == 4
