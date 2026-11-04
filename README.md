# 🐍 Warming-Up-for-Python
![Python logo](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

제가 공부하려고 만든 파이썬 학습 자료입니다. **파이썬 기초 → 코테용 노트 → 알고리즘 구현** 순서로 구성했습니다.

| 폴더 | 내용 | 이런 사람에게 |
| --- | --- | --- |
| [01_basics](./01_basics) | 파이썬 문법 기초 (Jupyter 노트북) | 파이썬이 처음 |
| [02_ps_notes](./02_ps_notes) | 코딩 테스트용 치트시트 | 다른 언어는 익숙하고, 코테 전에 파이썬을 훑고 싶음 |
| [03_algorithms](./03_algorithms) | 알고리즘·자료구조 구현 코드 | 특정 알고리즘 구현을 보고 싶음 |

---

## 01. Basics

순서대로 보면 됩니다.

1. [자료형](./01_basics/01_data_types.ipynb)
2. [제어문 (if)](./01_basics/02_control_flow.ipynb)
3. [반복문 (for, while)](./01_basics/03_loop.ipynb)
4. [문자열](./01_basics/04_string.ipynb)
5. [list · dict · set · tuple](./01_basics/05_list_dict_set_tuple.ipynb)
6. [내장 함수와 메서드](./01_basics/06_built_in_functions.ipynb)

## 02. PS Notes (코테 워밍업)

파이썬이 오랜만인 개발자가 코테 전에 훑어보는 노트입니다. 시간이 없으면 1 → 2 → 4 순서로.

| # | 노트 | 내용 |
| --- | --- | --- |
| 1 | [입출력과 함정](./02_ps_notes/01_io_and_pitfalls.md) | 빠른 입력 패턴, 출력, TLE 원인, 흔한 버그, 코테 템플릿 |
| 2 | [내장함수 치트시트](./02_ps_notes/02_builtins.md) | enumerate/zip/any/all, 정렬 key, 정수 연산 함정, 복사 |
| 3 | [문자열 다루기](./02_ps_notes/03_strings.md) | 찾기·자르기·치환·변환 (C++ string 대응) |
| 4 | [라이브러리](./02_ps_notes/04_libraries.md) | collections, heapq, bisect, itertools, functools, math, 상황별 추천 |
| 5 | [그래프 패턴](./02_ps_notes/05_graph_patterns.md) | BFS/DFS/격자 BFS/다익스트라/크루스칼 템플릿 |
| 6 | [인덱스·네이밍](./02_ps_notes/06_naming.md) | 루프 변수 이름 짓는 법 |

**이럴 땐 여기**
* 입력이 많아서 느리다 → [입출력과 함정 §1, §3](./02_ps_notes/01_io_and_pitfalls.md)
* 음수 나눗셈 / 반올림이 이상하다 → [내장함수 §6](./02_ps_notes/02_builtins.md#6-정수-연산-함정)
* 우선순위 큐 / lower_bound 가 필요하다 → [라이브러리 §2, §3](./02_ps_notes/04_libraries.md)
* C++ STL 의 무엇이 파이썬의 무엇인지 → [라이브러리 · 한눈에 보기](./02_ps_notes/04_libraries.md#한눈에-보기)

## 03. Algorithms

모든 파일은 단독 실행 가능합니다 (`python 03_algorithms/graph/dijkstra.py`). 일부는 표준 입력을 받습니다.

#### 정렬 `sorting/`
* [선택 정렬](./03_algorithms/sorting/selection_sort.py) · [삽입 정렬](./03_algorithms/sorting/insertion_sort.py) · [퀵 정렬](./03_algorithms/sorting/quick_sort.py) · [계수 정렬](./03_algorithms/sorting/counting_sort.py)
* [내장 정렬 사용법](./03_algorithms/sorting/sort_builtin.py)

#### 이진 탐색 `binary_search/`
* [이진 탐색](./03_algorithms/binary_search/binary_search.py)
* [bisect 사용법](./03_algorithms/binary_search/bisect_usage.py) — 이상/이하/초과/미만 위치 찾기
* [정렬된 배열에서 값이 [left, right] 인 원소 개수](./03_algorithms/binary_search/count_in_range.py)

#### 그래프 `graph/`
* [DFS & BFS](./03_algorithms/graph/dfs_bfs.py)
* [연결 요소 개수 (격자 BFS)](./03_algorithms/graph/connected_components.py)
* [다익스트라](./03_algorithms/graph/dijkstra.py)
* [최소 신장 트리 (Kruskal)](./03_algorithms/graph/mst.py)
* [위상 정렬](./03_algorithms/graph/topological_sort.py)
* [LCA (Binary Lifting)](./03_algorithms/graph/lca.py)
* [SCC (Tarjan)](./03_algorithms/graph/scc_tarjan.py)
* [단절점](./03_algorithms/graph/articulation_point.py)

#### 동적 계획법 `dp/`
* [LIS (O(N log N))](./03_algorithms/dp/lis.py)
* [비트마스크 TSP](./03_algorithms/dp/bitmask_tsp.py)

#### 문자열 `string/`
* [KMP](./03_algorithms/string/kmp.py)

#### 자료구조 `data_structure/`
* [Union-Find (Disjoint Set)](./03_algorithms/data_structure/disjoint_set.py)
* [좌표 압축](./03_algorithms/data_structure/coordinate_compression.py)
* [펜윅 트리 (BIT)](./03_algorithms/data_structure/fenwick_tree.py) — 구간 합 + 역전수 예제

#### 수학 `math/`
* [최대공약수 GCD](./03_algorithms/math/gcd.py) · [최소공배수 LCM](./03_algorithms/math/lcm.py) · [확장 유클리드](./03_algorithms/math/extended_euclidean.py)
* [소수 판정](./03_algorithms/math/is_prime.py) · [약수 구하기](./03_algorithms/math/divisors.py) · [소인수분해](./03_algorithms/math/prime_factorization.py)
* [뤼카 정리 (nCr mod p)](./03_algorithms/math/lucas_theorem.py)

#### 기하 `geometry/`
* [1차원 두 선분의 교점 개수](./03_algorithms/geometry/segment_intersection_1d.py)

#### 기법 `techniques/`
* [투 포인터 — 합이 M인 구간 개수](./03_algorithms/techniques/two_pointers.py)
* [누적 합](./03_algorithms/techniques/prefix_sum.py)
* [2차원 배열 90도 회전](./03_algorithms/techniques/rotate_matrix.py)
