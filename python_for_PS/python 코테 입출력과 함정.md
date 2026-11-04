# Python 코테 입출력 & 흔한 함정

> 로직은 맞는데 틀리거나 시간 초과가 나는 대부분의 원인 모음.

## 1. 입력 패턴 모음

```python
import sys
input = sys.stdin.readline

# 1) 정수 하나
n = int(input())

# 2) 정수 여러 개 (한 줄)
a, b = map(int, input().split())

# 3) 정수 리스트 (한 줄)
arr = list(map(int, input().split()))

# 4) n 줄에 걸친 정수
nums = [int(input()) for _ in range(n)]

# 5) n × m 격자 (공백 구분 숫자)
grid = [list(map(int, input().split())) for _ in range(n)]

# 6) n × m 격자 (붙어 있는 문자열: "0110")
board = [list(input().strip()) for _ in range(n)]
digits = [list(map(int, input().strip())) for _ in range(n)]

# 7) 문자열 한 줄 (개행 제거)
s = input().strip()

# 8) 입력 끝까지 읽기 (테스트케이스 수 미지정)
for line in sys.stdin:
    line = line.strip()
```

* `sys.stdin.readline` 은 개행(`\n`)을 포함해서 반환한다. 숫자는 `int()` 가 무시하지만 **문자열은 `.strip()` 필수**.
* `input = sys.stdin.readline` 으로 덮어쓰면 이후 `input()` 이 빠른 버전이 된다.

## 2. 출력 패턴 모음

```python
print(*arr)                       # 1 2 3
print(*arr, sep="\n")             # 한 줄씩
print(" ".join(map(str, arr)))    # 위와 동일 (join 은 문자열만 받음!)
print("YES" if ok else "NO")
print(f"{x:.2f}")                 # 소수점 둘째 자리 (3.14)
print(f"{x:05d}")                 # 00042
print(f"{x:>5}")                  # 오른쪽 정렬 폭 5
```

## 3. 시간 초과(TLE) 단골 원인

| 상황 | 느린 코드 | 개선 |
| --- | --- | --- |
| 입력이 많음 | `input()` | `sys.stdin.readline` |
| 앞에서 삭제/삽입 | `list.pop(0)`, `insert(0, x)` O(N) | `deque.popleft()` |
| 존재 여부 확인 반복 | `x in list` O(N) | `set` / `dict` 로 변환 (O(1)) |
| 문자열 누적 | `s += c` 를 수십만 번 | 리스트에 모아서 `"".join()` |
| 출력이 많음 | `print()` 반복 | 리스트에 모아 한 번에 출력 |
| 재귀 DFS | 깊이 제한 1000 | `setrecursionlimit(10**6)` 또는 스택으로 반복문 구현 |
| 2중 for 로 최솟값 | O(N²) | 정렬 + 투 포인터 / `heapq` / `bisect` |
| 리스트 슬라이스 반복 | `v[1:]` 를 재귀마다 | 인덱스(start, end)로 전달 (슬라이싱은 복사 O(N)) |

* 파이썬은 C++ 대비 대략 50~100배 느리다고 가정하고 연산량(약 1천만 번 이하)을 어림잡자.
* 같은 코드를 **PyPy3** 로 제출하면 반복문 위주 코드는 훨씬 빠르다 (단, 재귀는 PyPy 에서 메모리 주의).

## 4. 흔한 버그 모음

### 4-1. 변경 가능한 기본 인자

```python
def add(x, acc=[]):       # ❌ acc 가 호출 간에 공유됨
    acc.append(x)
    return acc
print(add(1), add(2))     # [1, 2] [1, 2]

def add2(x, acc=None):    # ✅
    acc = [] if acc is None else acc
    acc.append(x)
    return acc
```

### 4-2. 전역 변수 수정

```python
cnt = 0
def f():
    global cnt     # 없으면 UnboundLocalError
    cnt += 1
```

(리스트/딕셔너리의 *원소 수정* 은 `global` 없이 가능. 변수에 *재할당* 할 때만 필요.)

### 4-3. 반복 중 리스트 수정

```python
v = [1, 2, 3, 4]
for x in v:
    if x % 2 == 0:
        v.remove(x)      # ❌ 원소를 건너뜀
v = [x for x in v if x % 2]   # ✅ 새 리스트로
```

### 4-4. 문자열은 불변

```python
s = "hello"
# s[0] = 'H'      # ❌ TypeError
s = 'H' + s[1:]   # ✅ 새로 만들기
chars = list(s); chars[0] = 'J'; s = "".join(chars)   # 여러 번 바꿀 땐 리스트로
```

### 4-5. `is` vs `==`

값 비교는 `==`. `is` 는 같은 객체인지(주로 `None` 비교) 확인할 때만: `if x is None`.

### 4-6. 튜플 한 개짜리

```python
t = (1)     # int 1
t = (1,)    # 튜플
```

### 4-7. 정렬된 결과와 리스트 대입

```python
v = [3, 1, 2]
w = v.sort()      # w 는 None
w = sorted(v)     # 새 리스트
```

### 4-8. 딕셔너리/집합은 인덱스 접근 불가

`set` 은 순서가 없으므로 `s[0]` 불가. 하나 꺼내려면 `next(iter(s))` 또는 `s.pop()`.

### 4-9. 음수 인덱스와 슬라이싱 범위

```python
v = [1, 2, 3]
print(v[-1])       # 3 (마지막)
print(v[5:10])     # []  (슬라이스는 범위를 벗어나도 에러 X)
# print(v[5])      # IndexError
```

### 4-10. 정수 나눗셈과 모듈러

* `-7 // 2 == -4`, `-7 % 3 == 2` (C++ 와 다름, [내장함수 치트시트](./python%20%EB%82%B4%EC%9E%A5%ED%95%A8%EC%88%98%20%EC%B9%98%ED%8A%B8%EC%8B%9C%ED%8A%B8.md) 참고).

## 5. 자주 쓰는 초기값

```python
INF = float('inf')            # 또는 int(1e9), 10**18
dist = [INF] * (n + 1)
visited = [False] * (n + 1)
dp = [0] * (n + 1)
dp2 = [[0] * (m + 1) for _ in range(n + 1)]   # 2차원 (행마다 새 리스트!)

# 4방향 / 8방향 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < n and 0 <= ny < m:   # 범위 체크 (체이닝 비교)
        pass
```

## 6. 코테 템플릿

```python
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # TODO
    print(sum(arr))

if __name__ == "__main__":
    solve()
```

* 함수 안에서 실행하면 전역 변수 접근보다 약간 빠르다.
