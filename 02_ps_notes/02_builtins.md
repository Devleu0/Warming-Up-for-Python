# Python 내장함수 치트시트 (코테용)

> 다른 언어(C++/Java)에 익숙하고 파이썬은 오랜만인 사람을 위한 "이런 게 있었지?" 확인용 노트.
> 직접 짜기 전에 먼저 여기서 내장 기능이 있는지 확인하자.

## 한눈에 보기

| 하고 싶은 것 | 파이썬 | 비고 |
| --- | --- | --- |
| 인덱스 + 값 순회 | `for i, x in enumerate(v)` | `enumerate(v, 1)` 로 1부터 시작 |
| 두 리스트 동시 순회 | `for a, b in zip(v1, v2)` | 짧은 쪽 기준으로 종료 |
| 행/열 뒤집기 (전치) | `list(zip(*grid))` | 튜플 리스트가 나옴 |
| 하나라도 / 모두 만족 | `any(...)`, `all(...)` | 제너레이터와 함께 사용 |
| 몫과 나머지 | `q, r = divmod(a, b)` | |
| 거듭제곱 나머지 | `pow(a, b, mod)` | 빠른 거듭제곱 (직접 구현 불필요) |
| 모듈러 역원 | `pow(a, -1, mod)` | Python 3.8+ |
| 절댓값 | `abs(x)` | |
| 합 / 최대 / 최소 | `sum`, `max`, `min` | `key=`, `default=` 지원 |
| 뒤집기 | `reversed(v)`, `v[::-1]` | `reversed` 는 이터레이터 |
| 문자 ↔ 아스키 | `ord('a')`, `chr(97)` | |
| 진법 변환 | `bin(x)`, `oct(x)`, `hex(x)`, `int("101", 2)` | `bin(5)` → `'0b101'` |
| 올림/내림 | `math.ceil`, `math.floor` | `//` 는 내림 (음수 주의) |
| 무한대 | `float('inf')`, `-float('inf')` | |
| 두 값 교환 | `a, b = b, a` | temp 불필요 |

---

## 1. enumerate / zip

```python
v = ['a', 'b', 'c']

for i, x in enumerate(v):
    print(i, x)          # 0 a / 1 b / 2 c

for i, x in enumerate(v, 1):
    print(i, x)          # 1 a / 2 b / 3 c

names = ['kim', 'lee']
scores = [90, 80]
for n, s in zip(names, scores):
    print(n, s)          # kim 90 / lee 80

print(dict(zip(names, scores)))   # {'kim': 90, 'lee': 80}

grid = [[1, 2, 3], [4, 5, 6]]
print(list(zip(*grid)))           # [(1, 4), (2, 5), (3, 6)]  (전치)
print([list(r) for r in zip(*grid[::-1])])  # 시계 방향 90도 회전: [[4, 1], [5, 2], [6, 3]]
```

## 2. map / filter / 컴프리헨션

```python
nums = list(map(int, "1 2 3".split()))        # [1, 2, 3]
evens = list(filter(lambda x: x % 2 == 0, nums))   # [2]
evens2 = [x for x in nums if x % 2 == 0]      # 컴프리헨션이 더 파이썬스러움

squares = [x * x for x in range(5)]           # [0, 1, 4, 9, 16]
pairs = [(i, j) for i in range(2) for j in range(2)]  # [(0, 0), (0, 1), (1, 0), (1, 1)]
flat = [x for row in [[1, 2], [3, 4]] for x in row]   # [1, 2, 3, 4]  (2차원 → 1차원)
d = {x: x * x for x in range(3)}              # {0: 0, 1: 1, 2: 4}
s = {x % 3 for x in range(10)}                # {0, 1, 2}
```

## 3. any / all

```python
v = [1, 2, 3]
print(any(x > 2 for x in v))     # True
print(all(x > 0 for x in v))     # True
print(any([]), all([]))          # False True  (빈 리스트 주의)
```

## 4. sum / max / min 의 key, default

```python
words = ['apple', 'fig', 'banana']
print(max(words, key=len))            # 'banana'  (가장 긴 단어)
print(min(words, key=len))            # 'fig'
print(max([], default=-1))            # -1  (빈 시퀀스 에러 방지)
print(sum(len(w) for w in words))     # 14
print(sum([[1], [2]], []))            # [1, 2]  (리스트 이어붙이기, 느리니 작은 입력에만)

pts = [(1, 5), (3, 2)]
print(max(pts, key=lambda p: p[1]))   # (1, 5)
```

## 5. 정렬 심화 — sorted / sort / key

```python
v = [(1, 'b'), (2, 'a'), (1, 'a')]

print(sorted(v))                                  # [(1, 'a'), (1, 'b'), (2, 'a')]
print(sorted(v, key=lambda x: (-x[0], x[1])))     # 숫자 내림차순, 문자 오름차순
print(sorted(v, key=lambda x: x[1]))              # 안정 정렬(stable): 같은 키는 원래 순서 유지

words = ['banana', 'kiwi', 'apple']
print(sorted(words, key=lambda w: (len(w), w)))   # ['kiwi', 'apple', 'banana']
print(sorted(words, reverse=True))                # ['kiwi', 'banana', 'apple']
```

* `v.sort()` 는 제자리 정렬 후 `None` 반환. `v = v.sort()` 는 흔한 실수!
* 문자열 정렬 기준이 숫자 앞에 있으면 `key=int` 로 변환: `sorted(['10', '9', '2'], key=int)`.
* 커스텀 비교 함수가 꼭 필요하면 `functools.cmp_to_key` (→ [라이브러리](./04_libraries.md#5-functools)).

## 6. 정수 연산 함정

```python
print(7 // 2, -7 // 2)    # 3 -4   ← 내림(floor)! C++ 처럼 0 방향이 아님
print(7 % 3, -7 % 3)      # 1 2    ← 나머지는 항상 0 이상 (모듈러 연산에 편함)
print(int(-7 / 2))        # -3     ← 0 방향 나눗셈이 필요하면 int(a / b)
print(7 / 2)              # 3.5    ← / 는 항상 float
print(2 ** 100)           # 파이썬 int 는 오버플로우 없음 (long long 걱정 X)
print(round(2.5), round(3.5))   # 2 4  ← 짝수 쪽 반올림(banker's)! 사사오입 아님
print(0.1 + 0.2 == 0.3)         # False ← 실수 비교는 abs(a-b) < 1e-9
```

* 올림 나눗셈: `(a + b - 1) // b` 또는 `-(-a // b)`.
* 제곱근이 정수인지 판별: `math.isqrt(n) ** 2 == n` (`sqrt` 는 float 오차 가능).

## 7. 언패킹 / 슬라이싱 / 삼항

```python
a, *rest = [1, 2, 3, 4]       # a=1, rest=[2, 3, 4]
*init, last = [1, 2, 3]       # init=[1, 2], last=3
n, m = map(int, "3 4".split())

v = [0, 1, 2, 3, 4, 5]
print(v[1:4], v[:2], v[-2:], v[::2], v[::-1])
# [1, 2, 3] [0, 1] [4, 5] [0, 2, 4] [5, 4, 3, 2, 1, 0]

x = 5
msg = "홀수" if x % 2 else "짝수"     # 삼항 연산자
if 1 <= x <= 10: pass                   # 범위 비교 체이닝
```

## 8. 리스트 자주 쓰는 메서드

```python
v = [3, 1, 2]
v.append(4)          # 끝에 추가 O(1)
v.insert(0, 9)       # 앞에 삽입 O(N)  → 자주 쓰면 deque
v.pop()              # 끝 제거 O(1)
v.pop(0)             # 앞 제거 O(N)    → 자주 쓰면 deque.popleft()
v.remove(2)          # 값으로 첫 번째 제거 O(N)
v.extend([7, 8])     # 이어붙이기
v.index(7)           # 값의 위치 (없으면 ValueError)
v.count(7)           # 개수
del v[0]             # 인덱스로 삭제
print(len(v), 7 in v)   # `in` 은 리스트에서 O(N), set/dict 에서 O(1)
```

## 9. 얕은 복사 vs 깊은 복사

```python
a = [1, 2, 3]
b = a            # 같은 객체 (별칭)
c = a[:]         # 얕은 복사 (a.copy(), list(a) 도 동일)
b.append(4)
print(a, c)      # [1, 2, 3, 4] [1, 2, 3]

import copy
g = [[1, 2], [3, 4]]
h = g[:]                  # 바깥만 복사 → 안쪽 리스트는 공유됨!
k = copy.deepcopy(g)      # 안쪽까지 복사 (2차원 배열 복사는 이것)
# 또는 [row[:] for row in g]
```

## 10. 2차원 배열 초기화 함정

```python
n, m = 3, 4
bad = [[0] * m] * n                    # ❌ 모든 행이 같은 리스트를 가리킴
good = [[0] * m for _ in range(n)]     # ✅
bad[0][0] = 1
good[0][0] = 1
print(bad)    # [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
print(good)   # [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```

## 11. for-else, while-else

```python
for x in [1, 3, 5]:
    if x % 2 == 0:
        print("짝수 발견")
        break
else:                     # break 없이 끝났을 때만 실행
    print("짝수 없음")    # 출력됨
```

## 12. 문자 판별 메서드

```python
c = 'a'
print(c.isalpha(), c.isdigit(), c.isalnum(), c.isupper(), c.islower())
# True False True False True
print('12'.isdigit(), ' '.isspace())   # True True
print(ord('c') - ord('a'))             # 2   (알파벳 인덱스)
print(chr(ord('a') + 3))               # 'd'
```
