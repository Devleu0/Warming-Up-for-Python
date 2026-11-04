# 파이썬 라이브러리 (코테용)

> 코테에서 자주 쓰는 표준 라이브러리 모음. 위의 "한눈에 보기"에서 찾고, 필요한 절로 내려가서 예제를 보자.
> 빠른 입력(`sys.stdin.readline`)은 [입출력과 함정](./01_io_and_pitfalls.md), 깊은 복사(`copy.deepcopy`)는 [내장함수 치트시트](./02_builtins.md#9-얕은-복사-vs-깊은-복사)에 있다.

* **목차**
  * [한눈에 보기](#한눈에-보기)
  * [1. collections — deque / Counter / defaultdict](#1-collections)
  * [2. heapq — 우선순위 큐](#2-heapq)
  * [3. bisect — 이진 탐색](#3-bisect)
  * [4. itertools — 순열 / 조합 / 누적합](#4-itertools)
  * [5. functools — lru_cache / cmp_to_key / reduce](#5-functools)
  * [6. math](#6-math)
  * [7. re / string](#7-re--string)
  * [상황별 추천](#상황별-추천)
  * [파이썬에 없는 것](#파이썬에-없는-것)

## 한눈에 보기

| 자료구조 / 모듈 | C++ STL (참고) | 특징 | 시간복잡도 (평균) | 주요 메서드 |
| --- | --- | --- | --- | --- |
| `list` | `vector` | 동적 배열, 임의 접근 O(1) | `append` O(1), `insert`/`pop(i)` O(N) | `v.append(x)`, `v[i]`, `v.pop()` |
| `collections.deque` | `deque`, `queue` | 양방향 큐 | 양끝 삽입/삭제 O(1) | `q.popleft()`, `q.appendleft()` |
| `heapq` | `priority_queue` | 최소 힙 | `heappush`/`heappop` O(logN) | `heappush(pq, x)`, `heappop(pq)` |
| `set` | `unordered_set` | 중복 없는 집합 (해시) | O(1) | `s.add(x)`, `s.remove(x)`, `x in s` |
| `dict` | `unordered_map` | (key, value) (해시) | O(1) | `m[key] = val`, `key in m`, `m.get(key)` |
| `tuple` | `pair`, `tuple` | 불변 값 묶음 | O(1) | `t = (a, b)` |
| `collections.Counter` | `map<T, int>` | 개수 세기 특화 `dict` | O(1) | `Counter(v)`, `c.most_common()` |
| `collections.defaultdict` | - | 기본값 자동 생성 `dict` | O(1) | `defaultdict(list)`, `defaultdict(int)` |
| `bisect` | `lower_bound`, `upper_bound` | 정렬된 리스트 이진 탐색 | O(logN) | `bisect_left(v, x)` |
| `itertools` | `next_permutation` 등 | 순열/조합/누적합 | - | `permutations`, `combinations`, `accumulate` |
| `functools` | - | 메모이제이션, 커스텀 정렬 | - | `@lru_cache`, `cmp_to_key` |

* `list` 는 동적 배열이다. 앞쪽 삽입/삭제가 잦으면 `deque` 를 쓴다.
* `set`/`dict` 는 해시 기반(`unordered_*`). C++ `set`/`map` 같은 **정렬된** 자료구조는 없으므로, 정렬된 `list` + `bisect` 로 대신한다.

---

## 1. collections

### deque — 양방향 큐

양쪽 끝 추가/삭제가 O(1). 큐(BFS)·스택 모두 이걸로.

```python
from collections import deque

d = deque(['B', 'C'])
d.append('D')           # 오른쪽에 추가
d.appendleft('A')       # 왼쪽에 추가
print(d)                # deque(['A', 'B', 'C', 'D'])
d.pop()                 # 오른쪽에서 제거
d.popleft()             # 왼쪽에서 제거
print(d)                # deque(['B', 'C'])

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

### Counter — 개수 세기

```python
from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
c = Counter(words)
print(c)                     # Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(c.most_common(2))      # [('apple', 3), ('banana', 2)]
print(c.most_common(1)[0][0])    # 'apple'  (최빈값)
print(c['grape'])            # 0  (없는 키는 0, KeyError X)

a = Counter("aabbc")
b = Counter("abbbd")
print(a + b)             # Counter({'b': 5, 'a': 3, 'c': 1, 'd': 1})
print(a - b)             # Counter({'a': 1, 'c': 1})   (양수만 남음)
print(a & b)             # Counter({'b': 2, 'a': 1})   (교집합 = min)
print(a | b)             # 합집합 = max
print(list(a.elements()))                          # ['a', 'a', 'b', 'b', 'c']
print(Counter([1, 1, 2]) == Counter([2, 1, 1]))    # True  (구성이 같은지 비교, 애너그램 판별)
```

### defaultdict — 기본값 자동 생성

키가 없을 때 기본값을 자동 생성. 그래프 인접 리스트, 그룹핑에 필수.

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

* **주의:** 없는 키를 `graph[x]` 로 *읽기만* 해도 키가 생성된다. 존재 여부만 확인하려면 `x in graph`.

## 2. heapq

최소 힙. 일반 리스트를 힙처럼 다룬다. 다익스트라 등에 필수.

```python
import heapq

pq = []
heapq.heappush(pq, (3, "작업 C"))     # (우선순위, 값) — 튜플은 앞 원소부터 비교
heapq.heappush(pq, (1, "작업 A"))
heapq.heappush(pq, (2, "작업 B"))
print(pq[0])                          # (1, '작업 A')  (pop 하지 않고 최솟값 확인)
while pq:
    priority, task = heapq.heappop(pq)
    print(task)                       # 작업 A -> 작업 B -> 작업 C

v = [5, 1, 4, 2]
heapq.heapify(v)                      # 리스트를 O(N) 에 힙으로 변환 (제자리)
print(heapq.heappop(v))               # 1
print(heapq.nlargest(2, [5, 1, 4, 2]))     # [5, 4]
print(heapq.nsmallest(2, [5, 1, 4, 2]))    # [1, 2]

# 최대 힙: 부호를 바꿔서 넣고 꺼낼 때 다시 바꾼다
mx = []
for x in [3, 1, 4]:
    heapq.heappush(mx, -x)
print(-heapq.heappop(mx))             # 4
```

* `heapq` 는 최소 힙만 제공. 파이썬에 `priority_queue` 클래스는 없다.
* 힙 리스트를 출력하면 정렬된 순서가 아니다 (힙 구조). 맨 앞 `pq[0]` 만 최솟값이 보장된다.

## 3. bisect

정렬된 리스트에서 위치 찾기 / 정렬 유지 삽입.

* `bisect_left(a, x)`: x **이상**이 처음 나오는 위치 (C++ `lower_bound`)
* `bisect_right(a, x)`: x **초과**가 처음 나오는 위치 (C++ `upper_bound`)

```python
from bisect import bisect_left, bisect_right, insort

a = [10, 20, 30, 30, 40, 50]
print(bisect_left(a, 30))     # 2
print(bisect_right(a, 30))    # 4
print(bisect_right(a, 30) - bisect_left(a, 30))   # 2  (30의 개수)

# 값 범위 [lo, hi] 안의 개수
def count_in_range(arr, lo, hi):
    return bisect_right(arr, hi) - bisect_left(arr, lo)

print(count_in_range([1, 2, 2, 4, 7], 2, 4))    # 3

v = [1, 3, 5]
insort(v, 4)                  # 정렬 유지하며 삽입 (O(N))
print(v)                      # [1, 3, 4, 5]
```

* 파이썬 3.10+ 는 `key=` 인자도 지원.
* 직접 구현과 응용은 [03_algorithms/binary_search](../03_algorithms/binary_search/) 참고.

## 4. itertools

```python
from itertools import (permutations, combinations, product,
                       combinations_with_replacement, accumulate,
                       groupby, chain, zip_longest)
import operator

items = ['A', 'B', 'C']
print(list(permutations(items, 2)))   # 순열 nPr: [('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B')]
print(list(combinations(items, 2)))   # 조합 nCr: [('A','B'), ('A','C'), ('B','C')]
print(list(product('AB', repeat=2)))  # 중복 순열: [('A','A'), ('A','B'), ('B','A'), ('B','B')]
print(list(combinations_with_replacement('AB', 2)))   # 중복 조합 nHr: [('A','A'), ('A','B'), ('B','B')]

v = [1, 2, 3, 4]
print(list(accumulate(v)))                  # [1, 3, 6, 10]  (누적합)
print(list(accumulate(v, operator.mul)))    # [1, 2, 6, 24]  (누적곱)
print(list(accumulate(v, max)))             # [1, 2, 3, 4]   (누적 최댓값)

# groupby: 연속된 같은 값끼리 묶음 (정렬 안 하면 연속 구간 기준)
print([(k, len(list(g))) for k, g in groupby("aaabbc")])   # [('a', 3), ('b', 2), ('c', 1)]  (런-렝스 인코딩)

print(list(chain([1, 2], [3], [4, 5])))              # [1, 2, 3, 4, 5]
print(list(chain.from_iterable([[1, 2], [3, 4]])))   # [1, 2, 3, 4]  (2차원 → 1차원)
print(list(zip_longest([1, 2, 3], ['a'], fillvalue='-')))   # [(1, 'a'), (2, '-'), (3, '-')]
```

* `product` 는 여러 iterable 의 데카르트 곱도 된다: `product([1, 2], 'ab')`.
* 순열/조합은 이터레이터라서 `list()` 로 전부 만들면 메모리를 많이 쓴다. `for` 로 바로 순회하자.

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
* 재귀 깊이가 깊은 DP 는 `setrecursionlimit` 이 필요하고, 그래도 느리면 반복문(bottom-up)으로.

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

## 6. math

```python
import math

print(math.factorial(5))       # 120
print(math.sqrt(16))           # 4.0  (float)
print(math.isqrt(17))          # 4    (정수 제곱근, float 오차 없음)
print(math.gcd(12, 18, 24))    # 6    (3.9+ 는 여러 인자 가능)
print(math.lcm(4, 6))          # 12   (3.9+, 최소공배수)
print(math.comb(5, 2))         # 10   (nCr)
print(math.perm(5, 2))         # 20   (nPr)
print(math.ceil(2.1), math.floor(-2.1))   # 3 -3
print(math.inf > 10**18)       # True
print(math.hypot(3, 4))        # 5.0  (거리)
print(math.log2(8), math.log10(1000))     # 3.0 3.0
```

* `gcd`/`lcm` 은 직접 구현할 필요 없음 (원리는 [03_algorithms/math](../03_algorithms/math/) 참고).
* 모듈러 거듭제곱은 내장 `pow(a, b, MOD)` (`MOD = 10**9 + 7`).

## 7. re / string

```python
import re

print(re.findall(r'\d+', 'a12b345'))        # ['12', '345']   (숫자 덩어리 모두)
print(re.sub(r'[^a-z]', '', 'a1b2!c'))      # 'abc'           (소문자 외 제거)
print(re.split(r'[,\s]+', 'a, b  c,d'))     # ['a', 'b', 'c', 'd']
m = re.match(r'(\d+)-(\d+)', '10-20')
print(m.group(1), m.group(2))               # 10 20

import string
print(string.ascii_lowercase)    # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)             # 0123456789
```

---

## 상황별 추천

| 상황 | 추천 자료구조 / 모듈 |
| --- | --- |
| 스택 (LIFO) | `list` (`append`, `pop`) |
| 큐 (FIFO) / BFS | `collections.deque` (`append`, `popleft`) |
| 최소/최대 우선순위 | `heapq` (최소 힙), 부호 반전 (최대 힙) |
| 중복 없는 빠른 탐색 | `set`, `dict` |
| 개수 세기 | `Counter`, `defaultdict(int)` |
| 그래프 인접 리스트 | `defaultdict(list)` 또는 `[[] for _ in range(n + 1)]` |
| 정렬 상태에서 삽입/탐색 | `list` + `bisect` |
| 누적합 | `itertools.accumulate` 또는 직접 구현 |
| 순열 / 조합 | `itertools.permutations`, `combinations` |
| 좌표 압축 | `sorted(set(v))` 후 `dict` 로 매핑 |
| 메모이제이션 DP | `functools.lru_cache` |

## 파이썬에 없는 것

| C++/Java | 파이썬 대안 |
| --- | --- |
| `std::set` / `TreeSet` (정렬 집합) | 기본 제공 X → `bisect` + `list`, 필요시 `sortedcontainers` (코테 환경에서는 보통 불가) |
| `std::priority_queue` | `heapq` (최소 힙만) |
| `std::stack` | `list` (`append`, `pop`) |
| `std::queue` | `collections.deque` |
| `int` 오버플로우 | 없음 (임의 정밀도) |
| `switch` | `if/elif` 또는 `dict` (3.10+ 는 `match`) |
| `i++` | `i += 1` (`++` 없음) |
