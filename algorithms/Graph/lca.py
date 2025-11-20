import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

class LCA:
    def __init__(self, n, adj):
        self.n = n
        self.adj = adj
        self.depth = [0] * (n + 1)
        self.check = [False] * (n + 1)
        # parent[k][v] :: 정점 v의 2^k번째 조상
        # MAX_LOG는 2^k > N이 되는 넉넉한 값 (20이면 약 100만까지 커버)
        self.MAX_LOG = 20
        self.parent = [[0] * (n + 1) for _ in range(self.MAX_LOG)]

        # 1. DFS로 깊이(depth)와 직계 부모(parent[0]) 계산
        self._dfs(1, 0)
        
        # 2. DP로 희소 배열(Sparse Table) 채우기
        self._fill_parent()

    def _dfs(self, curr, d):
        self.check[curr] = True
        self.depth[curr] = d
        for next_node in self.adj[curr]:
            if not self.check[next_node]:
                self.parent[0][next_node] = curr
                self._dfs(next_node, d + 1)

    def _fill_parent(self):
        # 점화식: 2^k번째 조상은 (2^(k-1)번째 조상)의 (2^(k-1)번째 조상)과 같다
        for k in range(1, self.MAX_LOG):
            for v in range(1, self.n + 1):
                if self.parent[k-1][v] != 0:
                    self.parent[k][v] = self.parent[k-1][self.parent[k-1][v]]

    def get_lca(self, a, b):
        # 1. 깊이 맞추기: 더 깊은 쪽(b)을 a와 같은 높이로 올림
        if self.depth[a] > self.depth[b]:
            a, b = b, a
            
        # 깊이 차이만큼 b를 위로 올림
        for k in range(self.MAX_LOG - 1, -1, -1):
            if self.depth[b] - self.depth[a] >= (1 << k):
                b = self.parent[k][b]

        # 2. 이미 같다면 그게 LCA
        if a == b:
            return a

        # 3. 공통 조상 바로 아래까지 같이 올리기
        for k in range(self.MAX_LOG - 1, -1, -1):
            if self.parent[k][a] != self.parent[k][b]:
                a = self.parent[k][a]
                b = self.parent[k][b]

        # 4. 바로 위가 LCA
        return self.parent[0][a]

if __name__ == "__main__":
    # 예제 트리 구조 (1이 루트)
    #      1
    #    /   \
    #   2     3
    #  / \   /
    # 4   5 6
    
    N = 6
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
    adj_list = [[] for _ in range(N + 1)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    lca_solver = LCA(N, adj_list)

    print(f"LCA(4, 5) -> {lca_solver.get_lca(4, 5)}") # 예상: 2
    print(f"LCA(4, 6) -> {lca_solver.get_lca(4, 6)}") # 예상: 1
    print(f"LCA(3, 6) -> {lca_solver.get_lca(3, 6)}") # 예상: 3
