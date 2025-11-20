import sys

def get_pi(pattern):
    """
    실패 함수 (Failure Function) / Pi 배열 생성
    pi[i]: pattern[0...i] 접두사 중, 접두사이면서 동시에 접미사인 가장 긴 문자열의 길이
    """
    m = len(pattern)
    pi = [0] * m
    j = 0
    
    for i in range(1, m):
        # 일치하지 않으면 j를 이전 일치 상태로 되돌림
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        
        # 일치하면 j를 증가시키고 기록
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
            
    return pi

def kmp_search(text, pattern):
    """
    KMP 문자열 매칭 알고리즘
    :return: 매칭된 시작 인덱스들의 리스트
    """
    pi = get_pi(pattern)
    result = []
    n = len(text)
    m = len(pattern)
    j = 0
    
    for i in range(n):
        # 불일치 발생 시 실패 함수를 이용해 점프
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
            
        if text[i] == pattern[j]:
            # 패턴의 끝까지 모두 일치했다면
            if j == m - 1:
                # (i - m + 1)이 시작 인덱스
                result.append(i - m + 1)
                # 다음 매칭을 찾기 위해 j를 실패 함수 값으로 이동
                j = pi[j]
            else:
                j += 1
                
    return result, pi

if __name__ == "__main__":
    T = "ABABABABC"
    P = "ABAB"
    
    matches, pi_arr = kmp_search(T, P)
    
    print(f"텍스트: {T}")
    print(f"패턴: {P}")
    print(f"실패 함수(Pi): {pi_arr}") # ABAB -> [0, 0, 1, 2]
    print(f"매칭된 인덱스: {matches}") # 0, 2 (ABAB..., ..ABAB..)
    
    assert matches == [0, 2]
