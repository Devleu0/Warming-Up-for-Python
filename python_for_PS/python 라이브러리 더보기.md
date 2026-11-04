# Python 라이브러리 더보기 (코테용)

> [필수 라이브러리](./python%20%ED%95%84%EC%88%98%20%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC.md)에서 다룬
> `itertools(permutations/combinations/product)`, `heapq`, `bisect`, `deque`, `Counter`, `math` 이후에
> 코테에서 자주 쓰이는데 빠져 있던 것들.

| 라이브러리 | 용도 | 핵심 |
| --- | --- | --- |
| `collections.defaultdict` | 그래프, 그룹핑 | `defaultdict(list)`, `defaultdict(int)` |
| `itertools.accumulate` | 누적합 | `list(accumulate(v))` |
| `itertools.combinations_with_replacement` | 중복 조합 | |
| `itertools.groupby` | 연속된 같은 값 묶기 | 정렬 후 사용 |
| `itertools.chain` / `zip_longest` | 이어붙이기 / 길이 다른 zip | |
| `functools.lru_cache` | 메모이제이션 (DP) | `@lru_cache(None)` |
| `functools.cmp_to_key` | 커스텀 비교 정렬 | |
| `functools.reduce` | 누적 연산 | |
| `math` 추가 | `lcm`, `comb`, `isqrt`, `inf`, `ceil` | |
| `heapq` 추가 | `heapify`, `nlargest`, 최대 힙 | |
| `sys` | 빠른 입력, 재귀 한도 | `sys.stdin.readline` |
| `copy` | 깊은 복사 | `deepcopy` |
| `re` | 정규표현식 | 간단한 파싱 |

---

## 1. collections.defaultdict

키가 없을 때 기본값을 자동 생성. 그래프 인접 리스트, 개수 세기에 필수.

```python
from collections import defaultdict

graph = defaultdict(list)
graph[1].append(2)      # KeyError 없이 바로 append
graph[1].append(3)
graph[2].append(1)
print(dict(graph))      # {1: [2, 3], 2: [1]}

cnt = defaultdict(int)
for ch in "banana":
    cnt[ch] += 1
print(dict(cnt))        # {'b': 1, 'a': 3, 'n': 2}

groups = defaultdict(list)
for w in ["tea", "eat", "ate", "tan"]:
    groups[tuple(sorted(w))].append(w)    # 애너그램 묶기
print(list(groups.values()))              # [['tea', 'eat', 'ate'], ['tan']]
```

**주의:** 없는 키를 `graph[x]` 로 *읽기만* 해도 키가 생성된다. 존재 여부만 확인하려면 `x in graph`.

## 2. collections.deque 추가

```python
from collections import deque

d = deque([1, 2, 3, 4, 5])
d.rotate(2)             # 오른쪽으로 2칸 회전
print(d)                # deque([4, 5, 1, 2, 3])
d.rotate(-1)            # 왼쪽으로 1칸
print(d)                # deque([5, 1, 2, 3, 4])

window = deque(maxlen=3)    # 최대 길이 제한 (슬라이딩 윈도우)
for x in range(5):
    window.append(x)
print(window)           # deque([2, 3, 4], maxlen=3)

d.extendleft([9, 8])    # 왼쪽에 하나씩 넣으므로 순서가 뒤집힘
print(d)                # deque([8, 9, 5, 1, 2, 3, 4])
```

* 가운데 인덱스 접근 `d[i]` 는 O(N). 양끝 연산만 O(1).

## 3. collections.Counter 추가

```python
from collections import Counter

a = Counter("aabbc")
b = Counter("abbbd")
print(a + b)             # Counter({'b': 5, 'a': 3, 'c': 1, 'd': 1})
print(a - b)             # Counter({'a': 1, 'c': 1})   (양수만 남음)
print(a & b)             # Counter({'b': 2, 'a': 1})   (교집합 = min)
print(a | b)             # 합집합 = max

print(a['z'])            # 0  (없는 키는 0, KeyError X)
print(list(a.elements()))        # ['a', 'a', 'b', 'b', 'c']
print(a.most_common(1)[0][0])    # 'a'  (최빈값)
print(Counter([1, 1, 2]) == Counter([2, 1, 1]))   # True  (구성이 같은지 비교)
```

## 4. itertools 추가

```python
from itertools import accumulate, combinations_with_replacement, groupby, chain, zip_longest
import operator

v = [1, 2, 3, 4]
print(list(accumulate(v)))                  # [1, 3, 6, 10]  (누적합)
print(list(accumulate(v, operator.mul)))    # [1, 2, 6, 24]  (누적곱)
print(list(accumulate(v, max)))             # [1, 2, 3, 4]   (누적 최댓값)

print(list(combinations_with_replacement('AB', 2)))
# [('A', 'A'), ('A', 'B'), ('B', 'B')]      (중복 조합 nHr)

# groupby: 연속된 같은 값끼리 묶음 (정렬 안 하면 연속 구간 기준)
s = "aaabbc"
print([(k, len(list(g))) for k, g in groupby(s)])   # [('a', 3), ('b', 2), ('c', 1)]  (런-렝스 인코딩)

print(list(chain([1, 2], [3], [4, 5])))     # [1, 2, 3, 4, 5]
print(list(chain.from_iterable([[1, 2], [3, 4]])))  # [1, 2, 3, 4]  (2차원 → 1차원)
print(list(zip_longest([1, 2, 3], ['a'], fillvalue='-')))
# [(1, 'a'), (2, '-'), (3, '-')]
```

**팁:** `permutations`/`combinations`/`product` 는 이터레이터라서 `list()` 로 감싸 전부 만들면 메모리를 많이 쓴다. `for` 로 바로 순회하자.

## 5. functools

### lru_cache — 메모이제이션 한 줄로 DP

```python
from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

@lru_cache(maxsize=None)        # 3.9+ 는 @cache 도 가능
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(80))     # 23416728348467685
```

* 인자는 **해시 가능**해야 함 (리스트 X → 튜플로 변환).
* 재귀 깊이가 깊은 DP 는 `setrecursionlimit` 이 필요하고, 그래도 느리면 반복문(bottom-up) 으로.

### cmp_to_key — 비교 함수로 정렬

```python
from functools import cmp_to_key

# 이어붙여 가장 큰 수 만들기: "9" + "34" > "34" + "9"
def cmp(a, b):
    if a + b > b + a:
        return -1      # a 가 앞
    if a + b < b + a:
        return 1
    return 0

nums = ["3", "30", "34", "5", "9"]
nums.sort(key=cmp_to_key(cmp))
print("".join(nums))    # 9534330
```

### reduce

```python
from functools import reduce
import math
print(reduce(lambda a, b: a * b, [1, 2, 3, 4]))   # 24
print(reduce(math.gcd, [12, 18, 24]))             # 6  (여러 수의 최대공약수)
```

## 6. math 추가

```python
import math

print(math.lcm(4, 6))          # 12   (3.9+, 최소공배수)
print(math.gcd(12, 18, 24))    # 6    (3.9+ 는 여러 인자 가능)
print(math.comb(5, 2))         # 10   (nCr)
print(math.perm(5, 2))         # 20   (nPr)
print(math.isqrt(17))          # 4    (정수 제곱근, float 오차 없음)
print(math.ceil(2.1), math.floor(-2.1))   # 3 -3
print(math.inf > 10**18)       # True
print(math.hypot(3, 4))        # 5.0  (거리)
print(math.log2(8), math.log10(1000))     # 3.0 3.0
```

* 최대공약수 1줄이면 끝나므로 `gcd`/`lcm` 직접 구현은 불필요 (내 구현은 [algorithms/Number Theory](../algorithms/Number%20Theory/gcd.py) 참고).
* `10 ** 9 + 7` 같은 모듈러는 `MOD = 10**9 + 7`, `pow(a, b, MOD)`.

## 7. heapq 추가

```python
import heapq

v = [5, 1, 4, 2]
heapq.heapify(v)                 # 리스트를 O(N) 에 힙으로 변환 (제자리)
print(heapq.heappop(v))          # 1
print(heapq.nlargest(2, [5, 1, 4, 2]))    # [5, 4]
print(heapq.nsmallest(2, [5, 1, 4, 2]))   # [1, 2]

# 최대 힙: 부호를 바꿔서 넣고 꺼낼 때 다시 바꾼다
mx = []
for x in [3, 1, 4]:
    heapq.heappush(mx, -x)
print(-heapq.heappop(mx))        # 4

# 튜플은 앞 원소부터 비교 → (우선순위, 값)
pq = []
heapq.heappush(pq, (2, 'b'))
heapq.heappush(pq, (1, 'a'))
print(heapq.heappop(pq))         # (1, 'a')

print(v[0])                      # 최솟값 확인 (pop 하지 않고 peek)
```

* `heapq` 는 최소 힙만 제공. 파이썬에 `priority_queue` 클래스는 없다.
* 힙 내부 리스트를 출력하면 정렬된 순서가 아니다 (힙 구조).

## 8. sys — 빠른 입출력 / 재귀 한도

```python
import sys
input = sys.stdin.readline          # input() 보다 훨씬 빠름 (입력이 많을 때 필수)

n = int(input())                    # 개행 포함 문자열을 int() 가 알아서 처리
arr = list(map(int, input().split()))
s = input().strip()                 # 문자열은 개행 제거 필요 (rstrip())

data = sys.stdin.read().split()     # 전체 입력을 한 번에 토큰으로 (행 구분이 필요 없을 때)

sys.setrecursionlimit(10**6)        # DFS 재귀 깊이 (기본 1000)
print(sys.maxsize)                  # 9223372036854775807
```

출력도 많으면 모아서 한 번에:

```python
out = []
for i in range(3):
    out.append(str(i))
print("\n".join(out))         # 0\n1\n2
print(*[1, 2, 3])             # 1 2 3  (언패킹 출력)
print(*[1, 2, 3], sep="\n")   # 한 줄씩
print("a", end="")            # 줄바꿈 없이
```

## 9. copy

```python
import copy
g = [[1, 2], [3, 4]]
h = copy.deepcopy(g)
h[0][0] = 99
print(g[0][0])    # 1  (원본 유지)
```

## 10. re — 간단한 정규표현식

```python
import re

print(re.findall(r'\d+', 'a12b345'))        # ['12', '345']   (숫자 덩어리 모두)
print(re.sub(r'[^a-z]', '', 'a1b2!c'))      # 'abc'           (소문자 외 제거)
print(re.split(r'[,\s]+', 'a, b  c,d'))     # ['a', 'b', 'c', 'd']
m = re.match(r'(\d+)-(\d+)', '10-20')
print(m.group(1), m.group(2))               # 10 20
```

## 11. string 모듈

```python
import string
print(string.ascii_lowercase)    # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)             # 0123456789
```

## 12. bisect 추가

```python
import bisect

v = [1, 3, 5]
bisect.insort(v, 4)           # 정렬 유지하며 삽입 (O(N))
print(v)                      # [1, 3, 4, 5]

# 값 범위 [lo, hi] 안의 개수
def count_in_range(arr, lo, hi):
    return bisect.bisect_right(arr, hi) - bisect.bisect_left(arr, lo)

print(count_in_range([1, 2, 2, 4, 7], 2, 4))    # 3

# 파이썬 3.10+ 는 key= 인자도 지원
```

---

## 파이썬에 없는 것 (직접 구현/대안)

| C++/Java | 파이썬 대안 |
| --- | --- |
| `std::set` / `TreeSet` (정렬 집합) | 기본 제공 X → `bisect` + `list`, 필요시 `sortedcontainers` (코테 환경에서는 보통 불가) |
| `std::priority_queue` | `heapq` (최소 힙만) |
| `std::stack` | `list` (`append`, `pop`) |
| `std::queue` | `collections.deque` |
| `int` 오버플로우 | 없음 (임의 정밀도) |
| `switch` | `if/elif` 또는 `dict` (3.10+ 는 `match`) |
| `i++` | `i += 1` (`++` 없음) |
