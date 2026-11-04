# 🐍 Warming-Up-for-Python
![Python logo](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---
제가 공부하려고 만든 파이썬 기초 학습 자료입니다.

This repository contains my personal journey from **Python fundamentals** to **algorithm implementation**. It's designed for those who are new to Python or preparing for coding interviews.

### **구성**

#### Basics
* [자료형](./python_basics/data_types.ipynb)
* [반복문](./python_basics/loop.ipynb)
* [제어문](./python_basics/control_flow.ipynb)
* [Built_in_func&method.ipynb](./python_basics/Built_in_func%26method.ipynb)
* [문자열](./python_basics/string.ipynb)
* [list dict set tuple](./python_basics/collections(list_dict_set_tuple).ipynb)

#### Python for PS (코딩 테스트용 노트)
* [인덱스·네이밍](./python_for_PS/index_naming.md)
* [문자열 다루기](./python_for_PS/python%20%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%8B%A4%EB%A3%A8%EA%B8%B0.md)
* [알고리즘 공략](./python_for_PS/python%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B3%B5%EB%9E%B5.md)
* [필수 라이브러리](./python_for_PS/python%20%ED%95%84%EC%88%98%20%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC.md)

#### 정렬
* [선택 정렬](algorithms/Sorting/selection_sort.py)
* [삽입 정렬](algorithms/Sorting/insertion_sort.py)
* [퀵 정렬 / Quick Select](algorithms/Sorting/quick_sort.py)
* [Counting Sort](algorithms/Sorting/counting_sort.py)
* [Python Sort Library](algorithms/Sorting/python_sort_library.py)

#### 탐색
* [이진 탐색](algorithms/Searching/binary_search.py)
* [Bisect Library](algorithms/Searching/binary_search_library.py)
    * [Count the number of frequencies of elements whose value is between \[left, right\] in a sorted array](algorithms/Searching/count_the_number_of_frequencies_in_a_sorted_array.py)
    * [Find the number of connected components](algorithms/Searching/find_the_number_of_connected_components.py)
* [DFS & BFS](algorithms/Searching/dfs_and_bfs_example_1.py)
* [LIS_NlogN](algorithms/Searching/lis.py)
* [Bitmask_TSP](algorithms/Searching/Bitmask_TSP.py)
* [KMP_Algorithm](algorithms/Searching/KMP.py)

#### 그래프
* [다익스트라](algorithms/Graph/dijkstra.py)
* [DFS & BFS](algorithms/Searching/dfs_and_bfs_example_1.py)
* [MST](algorithms/Graph/mst.py)
* [Topology Sort](algorithms/Graph/topology_sort.py)
* [LCA_Binary_Lifting](algorithms/Graph/lca.py)
* [SCC_Tarjan](algorithms/Graph/scc_tarjan.py)
* [Articulation_Point](algorithms/Graph/articulation_point.py)

#### 자료 구조
* [Disjoint-Set (Union-Find)](algorithms/Data%20Structure/disjoint_set.py)
* [Coordinate_Compression](algorithms/Data%20Structure/coordinate_compression.py)
* [Fenwick_Tree](algorithms/Data%20Structure/fenwick_tree.py)

#### 수학
* [최대공약수 GCD](algorithms/Number%20Theory/gcd.py)
* [최소공배수 LCM](algorithms/Number%20Theory/lcm.py)
* [소수 판정](algorithms/Number%20Theory/is_prime_number.py)
* [약수 찾기](algorithms/Number%20Theory/find_all_divisors_of_a_number.py)
* [Prime Factorization](algorithms/Number%20Theory/prime_factorization.py)
* [확장 유클리드 호제법](algorithms/Number%20Theory/extended_euclidean.py)
* [Lucas 알고리즘](algorithms/Number%20Theory/lucas_theorem.py)

#### 기하
* [Number of intersection points of two lines in 1 dimension](algorithms/Geometry/number_of_intersection_points_of_two_lines_in_1_dimension.py)

#### 기타
* Two Pointers
    * [Number of intervals whose sum is M](algorithms/Miscellaneous/number_of_intervals_whose_sum_is_M.py)
* Interval Sum
    * [Prefix Sum](algorithms/Miscellaneous/prefix_sum.py)
    * [Fenwick Tree (Binary Indexed Tree)](algorithms/Miscellaneous/fenwick_tree.py)
* [Matrix Rotation](algorithms/Miscellaneous/rotate_a_matrix_by_90_degree.py)

---

### 개발 & 테스트

알고리즘 코드는 **import 해도 부작용이 없는 함수** + `if __name__ == "__main__":` 실행부 구조로 작성합니다.
(입력은 인자로 받고 결과는 `return`, 표준입력 처리는 `main()` 에 분리)

```bash
pip install -r requirements-dev.txt
pytest
```

새 알고리즘을 추가할 때는 `tests/` 에 테스트를 함께 추가해 주세요. 자세한 규칙은 [CONTRIBUTING.md](./CONTRIBUTING.md) 참고.
