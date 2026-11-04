from collections import deque
"""
위상 정렬 (Kahn's Algorithm)
    :param n: 노드 개수
    :param adj: 인접 리스트 (방향 그래프)
    :return: 정렬된 순서 리스트 (사이클 존재 시 빈 리스트 혹은 일부만 반환)
"""
def topological_sort(n, adj):
    indegree = [0] * (n + 1)
    
    # 1. 진입 차수 계산
    for u in range(1, n + 1):
        for v in adj[u]:
            indegree[v] += 1
            
    # 2. 진입 차수가 0인 노드를 큐에 삽입
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            
    result = []
    
    # 3. 큐가 빌 때까지 반복
    while queue:
        curr = queue.popleft()
        result.append(curr)
        
        for next_node in adj[curr]:
            indegree[next_node] -= 1
            # 새롭게 진입 차수가 0이 된 노드 등록
            if indegree[next_node] == 0:
                queue.append(next_node)
                
    # 결과 리스트의 길이가 N과 다르면 사이클 존재
    if len(result) != n:
        print("그래프에 사이클이 존재하여 위상 정렬 불가능")
        return []
        
    return result

if __name__ == "__main__":
    # 예제 입력
    # 1 -> 2
    # 1 -> 5
    # 2 -> 3
    # 3 -> 4
    # 5 -> 2 (1->5->2->3->4)
    # 6 (독립적)
    
    N = 6
    relations = [(1, 2), (1, 5), (2, 3), (3, 4), (5, 2)]
    # 독립된 노드 6을 위해 리스트 크기 조절
    adj_list = [[] for _ in range(N + 1)]
    
    for u, v in relations:
        adj_list[u].append(v)
    order = topological_sort(N, adj_list)
    print(f"위상 정렬 결과: {order}")
    # 가능한 답 중 하나: [1, 6, 5, 2, 3, 4] 또는 [6, 1, 5, 2, 3, 4] 등
