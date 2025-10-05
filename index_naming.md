# 인덱스 네이밍 가이드라인

인덱스는 코드의 **의도를 드러내는 가장 중요한 단서**다
문제 풀이 중 인덱스 실수를 줄이려면, 단순히 `i`, `j` 대신 **‘무엇을 순회하는 인덱스인지’** 이름으로 표현해야 한다.

---

## 기본 원칙

> **“이 인덱스가 무엇을 가리키는가?”**  
> 이름만 보고도 알 수 있게 작성하라.

- `i`, `j`, `k` : 의미 불분명
- `row`, `col`, `char_idx`, `left`, `right` : 역할 명확

---

## 상황별 권장 이름

| 상황 | 권장 이름 | 예시 코드 |
|------|-----------|-----------|
| 1차원 리스트 | `idx`, `value` | `for idx, value in enumerate(nums):` |
| 문자열 | `char_idx`, `char` | `for char_idx, char in enumerate(s):` |
| 2차원 배열 | `row`, `col` | `for row in range(n): for col in range(m):` |
| 투 포인터 (Two Pointer) | `left`, `right` / `start`, `end` | `while left < right:` |
| 이분 탐색 (Binary Search) | `lo`, `hi`, `mid` | `mid = (lo + hi) // 2` |
| 그래프 탐색 (DFS/BFS) | `cur_node`, `next_node` | `for next_node in graph[cur_node]:` |
| 경로 탐색 | `prev`, `cur`, `next_` | `next_ = path[cur]` |
| 정렬된 배열 | `sorted_idx`, `sorted_nums` | `for sorted_idx, val in enumerate(sorted(nums)):` |

---

## 이중 루프 구조

이중 루프에서는 `outer_` / `inner_` 접두어를 붙이거나 의미를 명시한다.

```python
for row in range(n):          # outer
    for col in range(m):      # inner
        grid[row][col]

또는

for outer_idx in range(n):
    for inner_idx in range(m):


---

상태 전이(DFS, BFS, DP 등)

cur_, next_ 접두어를 적극 활용하라.

cur_node = q.popleft()
for next_node in graph[cur_node]:
    if not visited[next_node]:
        visited[next_node] = True
        q.append(next_node)


---

# 기타 팁

## 한글로 생각하고 영어로 이름 짓기
예: "현재 좌표" → cur_x, cur_y
"다음 칸" → next_x, next_y

## 정렬, 변환, 복사된 데이터는 접두어 추가

sorted_nums, filtered_list, copied_arr


의미가 바뀌면 이름도 바꾼다

idx → left / right로 변할 때 즉시 변경




---

# 예시 비교

## 나쁜 예시

'''python
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            q.append((i, j))
'''

## 좋은 예시

'''python
for row in range(n):
    for col in range(m):
        if grid[row][col] == 1:
            q.append((row, col))
'''

---

# 결론

나쁜 이름	좋은 이름	의미

i, j	row, col	2차원 위치
x, y	cur_x, cur_y	현재 좌표
temp	next_value	다음 상태
n, m	num_rows, num_cols	크기 명확
arr2	sorted_arr	변환된 데이터



---

>  요약:
인덱스는 짧을 필요보다 명확할 필요가 있다.
이름만 바꿔도 디버깅 시간의 절반이 줄어든다.
