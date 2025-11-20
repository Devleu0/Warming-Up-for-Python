import sys
sys.setrecursionlimit(10**6)

class ArticulationPoint:
    def __init__(self, n, adj):
        self.n = n
        self.adj = adj
        self.order = [0] * (n + 1) # 방문 순서
        self.cnt = 0
        self.cut_vertex = set()    # 단절점 저장
        
        for i in range(1, n + 1):
            if self.order[i] == 0:
                self._dfs(i, True)

    def _dfs(self, curr, is_root):
        self.cnt += 1
        self.order[curr] = self.cnt
        
        # low: 내 자손들이 Back-edge를 통해 갈 수 있는 가장 빠른 방문 순서
        low = self.cnt 
        child_count = 0
        
        for next_node in self.adj[curr]:
            if self.order[next_node] != 0:
                # 이미 방문한 노드라면 (Back-edge)
                low = min(low, self.order[next_node])
            else:
                # 방문하지 않은 자식 노드
                child_count += 1
                
                # 자식 노드에서 DFS 수행 후, 그 자식이 도달 가능한 최소 순서 받아옴
                child_low = self._dfs(next_node, False)
                
                # 단절점 판별 조건 (루트가 아닐 때)
                # 자식이 우회로를 통해 내 조상(더 작은 번호)으로 갈 수 없다면
                # 즉, child_low가 내 방문 순서보다 크거나 같다면 나는 단절점
                if not is_root and child_low >= self.order[curr]:
                    self.cut_vertex.add(curr)
                
                low = min(low, child_low)
        
        # 루트 노드는 자식이 2명 이상이면 단절점
        if is_root and child_count >= 2:
            self.cut_vertex.add(curr)
            
        return low

if __name__ == "__main__":
    # 단절점 예제
    # 1-2-3 연결, 2-4 연결
    # 2를 지우면 {1, 3}과 {4}가 끊어짐 -> 2는 단절점
    
    N = 4
    edges = [(1, 2), (2, 3), (2, 4)]
    adj_list = [[] for _ in range(N + 1)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u) # 무방향 그래프
        
    ap = ArticulationPoint(N, adj_list)
    
    print(f"단절점 목록: {sorted(list(ap.cut_vertex))}")
    # 예상 결과: [2]
