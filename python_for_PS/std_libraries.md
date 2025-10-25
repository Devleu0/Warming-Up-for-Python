# 파이썬 필수 라이브러리 가이드
이 문서는 PS에 자주 사용되는 파이썬 표준 라이브러리의 핵심 기능과 간단한 예제를 제공합니다.

# 1. itertools: 효율적인 반복을 위한 도구
순열, 조합 등 복잡한 반복 작업 처리 

permutations(iterable, r): 순열
iterable에서 원소 r개를 뽑아 나열하는 모든 경우의 수(순서 고려 O)를 반환합니다.

예제 코드:
```
from itertools import permutations

items = ['A', 'B', 'C']

### items에서 2개를 뽑아 만들 수 있는 모든 순열
p = list(permutations(items, 2))
print(p)
```
#### 출력: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
* * *
combinations(iterable, r): 조합
iterable에서 원소 r개를 뽑는 모든 경우의 수(순서 고려 X)를 반환합니다.

예제 코드:
```
from itertools import combinations

items = ['A', 'B', 'C']

### items에서 2개를 뽑아 만들 수 있는 모든 조합
c = list(combinations(items, 2))
print(c)
```
#### 출력: [('A', 'B'), ('A', 'C'), ('B', 'C')]
* * *
product(*iterables, repeat=1): 중복 순열 (데카르트 곱)
여러 iterable에서 각각 하나씩 원소를 뽑아 만들 수 있는 모든 경우의 수를 반환합니다. repeat 인자를 사용하면 하나의 iterable에서 중복을 허용하여 뽑을 수 있습니다.

예제 코드:
```
from itertools import product

items = ['A', 'B']

### items에서 중복을 허용하여 2개를 뽑는 모든 경우 (중복 순열)
p = list(product(items, repeat=2))
print(p)
```
#### 출력: [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
* * *
* * *
# 2. heapq: 힙 및 우선순위 큐
최소 힙(min-heap) 제공, 우선순위 큐를 구현가능. 다익스트라(Dijkstra)와 같은 최단 경로 알고리즘에 필수적

특징: heapq는 일반적인 리스트를 힙처럼 다룰 수 있게 해줍니다.

heapq.heappush(heap, item): heap 리스트에 item을 추가합니다.

heapq.heappop(heap): heap 리스트에서 가장 작은 원소를 제거하고 반환합니다.

예제 코드 (우선순위 큐):
```
import heapq

### 비어 있는 리스트를 힙으로 사용
priority_queue = []

### 데이터 추가 (heappush)

heapq.heappush(priority_queue, (3, "작업 C")) # (우선순위, 값)
heapq.heappush(priority_queue, (1, "작업 A"))
heapq.heappush(priority_queue, (2, "작업 B"))

print(priority_queue) # 힙 구조로 정렬되어 있음

#### 출력: [(1, '작업 A'), (3, '작업 C'), (2, '작업 B')]

### 데이터 추출 (heappop) - 우선순위가 가장 높은(숫자가 가장 작은) 원소가 나옴
while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(f"수행할 작업: {task} (우선순위: {priority})")

#### 출력 순서: 작업 A -> 작업 B -> 작업 C
```
* * *
* * *
# 3. bisect: 이진 탐색
정렬된 리스트에 원소를 삽입하거나, 특정 값의 위치를 빠르게 찾을 때 사용

bisect_left(a, x): 정렬된 리스트 a에 x를 삽입할 가장 왼쪽 인덱스를 반환합니다.

bisect_right(a, x): 정렬된 리스트 a에 x를 삽입할 가장 오른쪽 인덱스를 반환합니다.

예제 코드:
```
from bisect import bisect_left, bisect_right

sorted_list = [10, 20, 30, 30, 40, 50]
value = 30

### value를 삽입할 가장 왼쪽 위치
left_idx = bisect_left(sorted_list, value)
print(f"{value}의 왼쪽 삽입 위치: {left_idx}") # 출력: 2

### value를 삽입할 가장 오른쪽 위치
right_idx = bisect_right(sorted_list, value)
print(f"{value}의 오른쪽 삽입 위치: {right_idx}") # 출력: 4

### 리스트에 특정 값의 개수 찾기
count = right_idx - left_idx
print(f"리스트 내 {value}의 개수: {count}") # 출력: 2
```
* * *
* * *
# 4. collections: 유용한 자료구조
기본 자료구조(list, dict 등)를 확장한 유용한 컨테이너들을 제공

deque: 양방향 큐
리스트와 달리 양쪽 끝에서 데이터를 추가하거나 제거하는 시간 복잡도가 O(1)으로 매우 빠릅니다. 큐(Queue)나 스택(Stack)으로 활용하기에 최적입니다.

예제 코드:
```
from collections import deque

d = deque(['B', 'C'])

d.append('D')        # 오른쪽에 추가
d.appendleft('A')    # 왼쪽에 추가
print(d)             # 출력: deque(['A', 'B', 'C', 'D'])

d.pop()              # 오른쪽에서 제거
d.popleft()          # 왼쪽에서 제거
print(d)             # 출력: deque(['B', 'C'])
```
Counter: 카운터
iterable 객체 내의 원소들의 개수를 세어 딕셔너리 형태로 반환합니다.
* * *
예제 코드:
```
from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

### 단어 빈도수 계산
word_counts = Counter(words)
print(word_counts)
#### 출력: Counter({'apple': 3, 'banana': 2, 'orange': 1})

### 가장 흔한 단어 2개 찾기
print(word_counts.most_common(2))
#### 출력: [('apple', 3), ('banana', 2)]
```
* * *
* * *
# 5. math: 수학 함수
기본적인 수학 연산 제공

factorial(x): x의 팩토리얼(x!)을 계산합니다.

sqrt(x): x의 제곱근을 계산합니다.

gcd(a, b): a와 b의 최대공약수(Greatest Common Divisor)를 계산합니다.

예제 코드:
```
import math

### 팩토리얼
print(f"5! = {math.factorial(5)}") # 출력: 120

### 제곱근
print(f"16의 제곱근 = {math.sqrt(16)}") # 출력: 4.0

### 최대공약수
print(f"48과 18의 최대공약수 = {math.gcd(48, 18)}") # 출력: 6
```
