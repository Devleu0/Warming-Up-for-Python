# 그래프 패턴 템플릿

> 코테에서 바로 꺼내 쓰는 그래프 탐색 뼈대 모음.
> 자료구조 선택은 [라이브러리](./04_libraries.md#상황별-추천), 전체 구현과 예제 입력은 [03_algorithms/graph](../03_algorithms/graph/) 참고.

* **목차**
  * [그래프 표현 방법](#그래프-표현-방법)
  * [BFS](#1-bfs-너비-우선-탐색)
  * [DFS](#2-dfs-깊이-우선-탐색)
  * [격자(2차원) BFS](#3-격자2차원-bfs)
  * [Dijkstra](#4-dijkstra-최단-경로)
  * [Kruskal (MST)](#5-kruskal-mst)

## 그래프 표현 방법

| 용도 | 자료구조 | 코드 |
| --- | --- | --- |
| 인접 리스트 | `defaultdict(list)` 또는 2차원 리스트 | `graph = defaultdict(list); graph[u].append(v)` |
| 방향/무방향 | 인접 리스트 | `g[u].append(v)` (단방향), `g[v].append(u)` 추가 시 양방향 |
| 가중치 그래프 | 인접 리스트 + `tuple` | `graph[u].append((v, w))` (노드, 가중치) |
| 간선 리스트 | `list[tuple]` | Kruskal: `edges.append((w, u, v))` |
| 방문 체크 | `list[bool]` 또는 `set` | `visited = [False] * (n + 1)` |
| BFS 레벨 | `deque[tuple]` | `q.append((node, depth))` |

---

## 1. BFS (너비 우선 탐색)

```python
from collections import deque, defaultdict

graph = defaultdict(list)
visited = [False] * (n + 1)    # n: 노드 개수

def bfs(start):
    q = deque([start])
    visited[start] = True      # 넣을 때 방문 처리 (중복 삽입 방지)
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
```

## 2. DFS (깊이 우선 탐색)

```python
import sys
sys.setrecursionlimit(10**6)   # 재귀 깊이 제한 (기본 1000)

graph = defaultdict(list)
visited = [False] * (n + 1)

def dfs(cur):
    visited[cur] = True
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt)
```

## 3. 격자(2차원) BFS

```python
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    dist = [[-1] * m for _ in range(n)]
    dist[sx][sy] = 0
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist
```

* 연결 요소 개수 세기 예제: [connected_components.py](../03_algorithms/graph/connected_components.py)

## 4. Dijkstra (최단 경로)

```python
import heapq
from collections import defaultdict

graph = defaultdict(list)          # graph[u] = [(v, w), ...]
dist = [float('inf')] * (n + 1)

def dijkstra(start):
    pq = [(0, start)]              # (비용, 노드) — 최소 힙
    dist[start] = 0
    while pq:
        cost, cur = heapq.heappop(pq)
        if cost > dist[cur]:       # 이미 더 짧은 경로로 처리됨
            continue
        for nxt, weight in graph[cur]:
            new_cost = cost + weight
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))
```

## 5. Kruskal (MST)

```python
edges = []                         # (가중치, u, v)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])   # 경로 압축
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False
    parent[b] = a
    return True

def kruskal(n):
    global parent
    parent = list(range(n + 1))
    total_cost = 0
    for w, u, v in sorted(edges):  # 가중치 오름차순
        if union(u, v):
            total_cost += w
    return total_cost
```

* Union-Find 자체는 [disjoint_set.py](../03_algorithms/data_structure/disjoint_set.py) 참고.
