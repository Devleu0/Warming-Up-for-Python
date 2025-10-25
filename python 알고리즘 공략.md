# Python Problem Solving 공략

* **목차**
  * [주요 컨테이너](#1.%20주요%20컨테이너)
  * [내장 함수 및 주요 모듈](#2.%20내장%20함수%20및%20주요%20모듈)
  * [문자열 관련 메서드](#3.%20문자열%20관련%20메서드)
  * [그래프 패턴](#4.%20그래프%20패턴%20(`defaultdict`,%20`deque`,%20`heapq`))
  * [자주 쓰는 조합](#5.%20자주%20쓰는%20조합)
  * [자료구조 팁](#자료구조%20팁)

## 1. 주요 컨테이너

| 자료구조 / 모듈        | C++ STL (참고)   | 특징                            | 시간복잡도 (평균)                    | 주요 메서드 / 패턴                                  |
| -------------------- | ----------------- | -------------------------------- | --------------------------------- | ------------------------------------------------ |
| `list`               | `vector`         | 동적 배열, 임의 접근 O(1)           | `append` O(1), `insert`/`pop(i)` O(N) | `v.append(x)`, `v[i]`, `v.pop()`                  |
| `collections.deque`  | `deque`, `queue`  | 양방향 큐                       | 양끝 삽입/삭제 O(1)                  | `q.popleft()`, `q.appendleft()`     |
| `heapq` 모듈         | `priority_queue`  | 최소 힙           | `heappush`/`heappop` O(logN)         | `heappush(pq, x)`, `heappop(pq)`                  |
| `set`               | `unordered_set`  | 중복 없는 집합       | 평균 O(1)                           | `s.add(x)`, `s.remove(x)`, `x in s`               |
| `dict`               | `unordered_map`  | (key, value)           | 평균 O(1)                           | `m[key] = val`, `key in m`, `m.get(key)`           |
| `tuple`              | `pair`, `tuple`  | 불변(immutable) 값 묶음           | O(1)                              | `t = (a, b)`                   |
| `collections.Counter` | `map<T, int>`    | 개수 카운팅 특화 `dict`           | O(1)                              | `Counter(list)`, `c.most_common()`                |
| `collections.defaultdict` | -               | 기본값 자동 생성 `dict` (그래프)     | O(1)                              | `defaultdict(list)`, `defaultdict(int)`          |

**참고** 

Python의 list는 내부적으로 C 배열과 유사하게 연속 메모리 + 포인터 배열 구조, 즉 이론적으로는 동적 배열. 따라서 앞뒤 삽입/삭제가 자주 필요하다면 deque를 사용

Python의 `set`/`dict`는 C++의 `unordered_set`/`unordered_map`처럼 해시 기반.
C++의 `set`/`map`과 같은 정렬된(tree) 자료구조가 필요하면, `list`를 정렬 후 `bisect` 모듈을 사용해야 함.

-----

## 2. 내장 함수 및 주요 모듈

| 함수                               | 기능                |                                                         |
| -------------------------------- | -------------------------- | --------------------------------------------------------- |
| `sorted(iterable)`               | 오름차순 정렬 반환 | `new_v = sorted(v)`                                  |
| `list.sort()`                     | 오름차순 정렬 변환 | `v.sort()`                                          |
| `sorted(..., reverse=True)`       | 내림차순 정렬           | `v.sort(reverse=True)`                                |
| `list.reverse()`, `list[::-1]`     | 순서 반전             | `v.reverse()` (인플레이스), `new_v = v[::-1]` (새 리스트)     |
| `max(iterable)`, `min(iterable)`   | 최댓값, 최솟값 반환       | `max(v)`, `min(v)`                                    |
| `sum(iterable, start=0)`         | 합계 (C++ `accumulate`) | `sum(v)`, `sum(v, 10)`                                 |
| `list.count(val)`                | 특정 값 개수           | `v.count(3)`                                       |
| `val in list`, `list.index(val)` | 값 찾기              | `if x in v: ...`, `idx = v.index(x)` (없으면 Error)    |
| `bisect.bisect_left(v, x)`       | x 이상 첫 위치 (이진 탐색) | `idx = bisect.bisect_left(v, x)`                        |
| `bisect.bisect_right(v, x)`      | x 초과 첫 위치         | `idx = bisect.bisect_right(v, x)`                       |
| `list(dict.fromkeys(v))`          | 중복 제거 (순서 유지)      | `v = list(dict.fromkeys(v))` (Python 3.7+)                |
| `itertools.permutations(v, r)`  | 순열 (nPr)          | `for p in permutations(v, 2): ...`                      |
| `itertools.combinations(v, r)`  | 조합 (nCr)          | `for c in combinations(v, 2): ...`                      |

-----

## 3. 문자열 관련 메서드

| 메서드                 | 설명          |                          |
| ------------------ | ----------- | -------------------------- |
| Slicing `s[start:end]` | 부분 문자열      | `s[2:5]`, `s[:3]`, `s[1:]`   |
| `find(sub)`, `rfind(sub)` | 부분 문자열 위치 (없으면 -1) | `s.find("abc")`            |
| `startswith(sub)`, `endswith(sub)` | 시작/끝 문자열 | `s.startswith("http")`     |
| `==`, `<`, `>`      | 문자열 비교      | `if s1 == s2:`              |
| `int()`, `float()`   | 문자열 → 숫자    | `int("123")`               |
| `str()`             | 숫자 → 문자열    | `str(42)`                 |
| `split(sep=None)`    | 공백/기준 단위 split | `s.split()`, `s.split(',')`  |
| `sep.join(iterable)` | 리스트 → 문자열 join | `"-".join(["a", "b", "c"])` |
| `replace(old, new)`  | 문자열 치환      | `s.replace(" ", "_")`       |

-----

## 4. 그래프 패턴 (`defaultdict`, `deque`, `heapq`)

| 용도              | 자료구조                                                              |  코드                                                                    |
| --------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 인접 리스트          | `collections.defaultdict(list)` (추천)                            | `graph = defaultdict(list); graph[u].append(v)`                      |
| 방문 체크           | `list[bool]` 또는 `set`                                            | `visited = [False] * (n+1)` 또는 `visited = set()`                    |
| 큐 BFS           | `collections.deque`                                             | `q = deque([start])`                                                   |
| DFS 재귀          | 재귀 함수                                                     | `def dfs(cur): for nxt in graph[cur]: if not visited[nxt]: ...` |
| 가중치 그래프         | `defaultdict(list)` + `tuple`                                    | `graph[u].append((v, w))` (노드, 가중치)                            |
| 최단경로 (Dijkstra) | `heapq` 모듈                                                    | `pq = [(0, start)]; heappush(pq, (dist, node))`                       |
| 간선 리스트          | `list[tuple]`                                                 | Kruskal: `edges.append((w, u, v))`                                  |
| BFS 레벨          | `deque[tuple]`                                                | `q.append((node, depth))`                                           |
| 방향/무방향 그래프      | `defaultdict(list)`                                             | `g[u].append(v)` (단방향), `g[v].append(u)` (양방향 추가)              |

-----

\<details\> \<summary\>`1: BFS (너비 우선 탐색)`\</summary\>

```python
from collections import deque, defaultdict

graph = defaultdict(list)
visited = [False] * (n + 1) # n: 노드 개수

def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
```

\</details\>

\<details\> \<summary\>`2: DFS (깊이 우선 탐색)`\</summary\>

```python
import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 설정

graph = defaultdict(list)
visited = [False] * (n + 1)

def dfs(cur):
    visited[cur] = True
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt)
```

\</details\>T

\<details\>\<summary\> `3: Dijkstra (최단 경로)`\</summary\>

```python
import heapq
from collections import defaultdict

graph = defaultdict(list)
dist = [float('inf')] * (n + 1)

def dijkstra(start):
    pq = [(0, start)] # (비용, 노드) - 최소 힙
    dist[start] = 0

    while pq:
        cost, cur = heapq.heappop(pq)
        if cost > dist[cur]:
            continue

        for nxt, weight in graph[cur]:
            new_cost = cost + weight
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))
```

\</details\>

\<details\>\<summary\>`4: Kruskal (MST)`\</summary\>

```python
edges = [] # (가중치, u, v) 튜플 저장
parent = []

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def unite(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        return True
    return False

def kruskal(n):
    edges.sort() # 가중치 기준 오름차순 정렬
    global parent
    parent = list(range(n + 1))
    
    total_cost = 0
    for w, u, v in edges:
        if unite(u, v):
            total_cost += w
    return total_cost
```

\</details\>

-----

## 5. 자주 쓰는 조합

### 1) 우선순위 큐 (최소 힙 / 최대 힙)

```python
import heapq
min_pq = []
heapq.heappush(min_pq, 3)
heapq.heappush(min_pq, 1)
print(heapq.heappop(min_pq)) # 1 (최소 힙)

max_pq = []
heapq.heappush(max_pq, -3) # 값에 -1 곱하기
heapq.heappush(max_pq, -1)
print(-heapq.heappop(max_pq)) # 1 (최대 힙)
```

### 2) 튜플/리스트 정렬 (다중 기준)

```python
v = [(1, 5), (0, 3), (1, 2)]
# 0번 인덱스 오름차순, 0번이 같으면 1번 인덱스 내림차순
v.sort(key=lambda x: (x[0], -x[1]))
# v = [(0, 3), (1, 5), (1, 2)]
```

### 3) 리스트 중복 제거 (순서 유지)

```python
v = [1, 3, 2, 3, 1, 2, 5]
v_unique = list(dict.fromkeys(v)) # [1, 3, 2, 5] (Python 3.7+)
```

### 4) 이진 탐색으로 인덱스 찾기 (`bisect`)

```python
import bisect
v = [1, 2, 4, 4, 6, 7]
# 4 이상이 처음 나오는 인덱스 (lower_bound)
idx = bisect.bisect_left(v, 4) # 2
# 4 초과가 처음 나오는 인덱스 (upper_bound)
idx2 = bisect.bisect_right(v, 4) # 4
```

### 5) 문자열 split (공백/특정 문자)

```python
s = "apple orange banana"
res = s.split() # ['apple', 'orange', 'banana']

s2 = "2025-10-25"
res2 = s2.split('-') # ['2025', '10', '25']
# 숫자로 변환
nums = list(map(int, res2)) # [2025, 10, 25]
```

### 6) 2차원 배열 초기화

```python
n, m = 5, 4
# 잘못된 방법 (내부 리스트가 모두 동일 객체)
# board = [[0] * m] * n 
# 올바른 방법 (리스트 컴프리헨션)
board = [[0 for _ in range(m)] for _ in range(n)]
```

-----

## 기타 자주 쓰는 모듈

| 모듈                                   |  기능                                 |
| ------------------------------------ | ------------------------------------- |
| `sys`                             | `sys.stdin.readline` (빠른 입력), `sys.setrecursionlimit` |
| `math`                           | `sqrt`, `pow`, `ceil`, `floor`, `gcd` (최대공약수) |
| `itertools`                       | `permutations` (순열), `combinations` (조합), `accumulate` (누적합) |
| `re`                              | 정규 표현식                                 |
| `string`                         | `string.ascii_lowercase` (알파벳 상수)        |

-----

## 자료구조 팁

| 상황           | 추천 자료구조 / 모듈                                |
| ------------ | ------------------------------------------------- |
| 그래프 탐색       | `collections.defaultdict(list)`, `collections.deque`   |
| 가중치 그래프      | `defaultdict(list)` + `tuple`, `heapq` (다익스트라)  |
| 최소 스패닝 트리    | `list` (간선 저장), `sort()`, `find-union` (Disjoint Set) |
| 중복 없는 빠른 탐색  | `set`, `dict` (해시 기반)                        |
| 문자열 분리/결합    | `split()`, `join()`                            |
| 누적합          | `itertools.accumulate` 또는 직접 `list` 구현        |
| 순열 / 조합      | `itertools.permutations`, `itertools.combinations`    |
| 좌표 압축        | `sorted(list(set(coords)))` 후 `dict`로 매핑         |
| 스택 (LIFO)      | `list` (`append`, `pop`)                          |
| 큐 (FIFO)       | `collections.deque` (`append`, `popleft`)         |
| 최소/최대 우선순위      | `heapq` (최소 힙), `heapq` + 부호 반전 (최대 힙)    |
| 개수 세기         | `collections.Counter`, `collections.defaultdict(int)` |
| 정렬 상태에서 삽입/탐색 | `list` + `bisect` 모듈                        |






