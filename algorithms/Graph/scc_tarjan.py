import sys
sys.setrecursionlimit(10**6)

class TarjanSCC:
    def __init__(self, n, adj):
        self.n = n
        self.adj = adj
        self.id = 0
        self.d = [0] * (n + 1)      # 방문 순서 (Discovery Time)
        self.finished = [False] * (n + 1) # SCC 확정 여부
        self.stack = []
        self.scc_result = []
        
        for i in range(1, n + 1):
            if self.d[i] == 0:
                self._dfs(i)

    def _dfs(self, u):
        self.id += 1
        self.d[u] = self.id  # 방문 순서 기록
        self.stack.append(u)
        
        parent = self.d[u]
        
        for v in self.adj[u]:
            # 1. 아직 방문하지 않은 이웃 -> DFS 진행
            if self.d[v] == 0:
                parent = min(parent, self._dfs(v))
            # 2. 방문은 했지만 아직 SCC가 확정되지 않은 이웃 (스택에 있음)
            # -> 현재 노드 u에서 v로 갈 수 있고, v도 u의 조상이므로 사이클 발생
            elif not self.finished[v]:
                parent = min(parent, self.d[v])
                
        # 3. 부모 노드가 자기 자신인 경우 -> SCC 발견
        # (즉, 내 자손들이 내 조상으로 올라가는 경로가 없음)
        if parent == self.d[u]:
            current_scc = []
            while True:
                t = self.stack.pop()
                self.finished[t] = True
                current_scc.append(t)
                if t == u:
                    break
            self.scc_result.append(sorted(current_scc))
            
        return parent

if __name__ == "__main__":
    # SCC 예제
    # 1 -> 2 -> 3 -> 1 (사이클: 1,2,3)
    # 3 -> 4 -> 5 -> 4 (사이클: 4,5)
    # 5 -> 6 (독립: 6)
    
    N = 6
    edges = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 4), (5, 6)]
    adj_list = [[] for _ in range(N + 1)]
    for u, v in edges:
        adj_list[u].append(v)
        
    solver = TarjanSCC(N, adj_list)
    
    print(f"찾은 SCC 개수: {len(solver.scc_result)}")
    print(f"SCC 구성: {solver.scc_result}")
    # 예상 결과: [[6], [4, 5], [1, 2, 3]] (순서는 다를 수 있음)
