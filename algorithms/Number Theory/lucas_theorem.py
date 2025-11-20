import sys

# 1. 기본적인 거듭제곱 (분할 정복)
def power(a, b, m):
    res = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b //= 2
    return res

# 2. 페르마의 소정리를 이용한 nCr (P가 소수일 때)
class Combination:
    def __init__(self, max_n, mod):
        self.mod = mod
        self.fact = [1] * (max_n + 1)
        
        # 팩토리얼 전처리
        for i in range(2, max_n + 1):
            self.fact[i] = (self.fact[i-1] * i) % mod

    def nCr(self, n, r):
        if r < 0 or r > n:
            return 0
        
        # nCr = n! / (r! * (n-r)!) % mod
        # 분모의 역원 = (r! * (n-r)!)^(mod-2) % mod
        numerator = self.fact[n]
        denominator = (self.fact[r] * self.fact[n-r]) % self.mod
        
        return (numerator * power(denominator, self.mod - 2, self.mod)) % self.mod

# 3. 뤼카의 정리 (Lucas Theorem)
# N, R이 매우 크고 P가 작을 때 사용
def lucas_theorem(n, r, p):
    if r == 0:
        return 1
    
    # nCr % p = (n%p C r%p) * (n//p C r//p) % p
    # 즉, P진법으로 나타냈을 때 각 자릿수의 조합의 곱
    
    # n % p C r % p 계산 (작은 범위의 조합)
    current_n = n % p
    current_r = r % p
    
    if current_r > current_n:
        return 0
    
    # 작은 범위는 직접 계산하거나 DP 사용 (여기서는 단순 계산)
    # 실제로는 위 Combination 클래스와 함께 사용하여 효율 높임
    numerator = 1
    denominator = 1
    for i in range(current_r):
        numerator = (numerator * (current_n - i)) % p
        denominator = (denominator * (i + 1)) % p
        
    base_comb = (numerator * power(denominator, p - 2, p)) % p
    
    # 재귀 호출 (다음 자릿수)
    return (base_comb * lucas_theorem(n // p, r // p, p)) % p

if __name__ == "__main__":
    MOD = 13 # 작은 소수 예시
    
    # Case 1: 일반 조합 (Fermat)
    # 100개의 아이템 중 2개를 고르는 경우의 수 % 13
    solver = Combination(100, MOD)
    res_fermat = solver.nCr(5, 2) # 10 -> 10 % 13 = 10
    print(f"[Fermat] 5C2 % {MOD} = {res_fermat}") # 10
    
    # Case 2: 뤼카의 정리
    # n, r이 매우 클 때: 100C5 % 13
    # 100 = 7*13 + 9,  5 = 0*13 + 5
    # lucas(100, 5) = lucas(7, 0) * 9C5 % 13
    res_lucas = lucas_theorem(100, 5, MOD)
    print(f"[Lucas] 100C5 % {MOD} = {res_lucas}")
