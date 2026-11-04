def extended_gcd(a, b):
    """
    확장 유클리드 호제법 (Extended Euclidean Algorithm)
    ax + by = gcd(a, b) 를 만족하는 (g, x, y)를 반환
    :return: (gcd(a, b), x, y)
    """
    if b == 0:
        # base case: a*1 + 0*0 = a (gcd는 a)
        return a, 1, 0
    
    # Recursive step
    g, x1, y1 = extended_gcd(b, a % b)
    
    # 유도 과정:
    # b*x1 + (a%b) *y1 = g
    # b*x1 + (a - (a//b) *b) *y1 = g
    # a*y1 + b* (x1 - (a//b) *y1) = g
    # 따라서 x = y1, y = x1 - (a//b) *y1
    x = y1
    y = x1 - (a // b) * y1
    
    return g, x, y

def mod_inverse(a, m):
    """
    모듈러 역원 구하기 (Modular Inverse)
    a * x ≡ 1 (mod m) 인 x를 반환. (없으면 None)
    """
    g, x, y = extended_gcd(a, m)
    
    if g != 1:
        return None # 역원이 존재하지 않음 (a와 m이 서로소가 아님)
    
    # x가 음수일 수 있으므로 m을 더해 양수로 변환
    return (x % m + m) % m

if __name__ == "__main__":
    # 예제 1: 3x + 11y = gcd(3, 11) = 1 만족하는 x, y 찾기
    a, b = 3, 11
    g, x, y = extended_gcd(a, b)
    print(f"Extended GCD({a}, {b}) -> GCD: {g}, x: {x}, y: {y}")
    print(f"검증: {a}*{x} + {b}*{y} = {a*x + b*y}")
    
    # 예제 2: 모듈러 역원 구하기
    # 3 * x ≡ 1 (mod 11) -> x는?
    inv = mod_inverse(a, b)
    print(f"\n{a}의 mod {b} 역원: {inv}") # 3 * 4 = 12 ≡ 1 (mod 11) 이므로 4 예상
    
    assert (a * inv) % b == 1
