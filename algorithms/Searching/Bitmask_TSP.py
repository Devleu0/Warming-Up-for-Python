import sys

"""
외판원 순회 (Traveling Salesman Problem)
    :param n: 도시의 수 (최대 16 정도 권장)
    :param w: 비용 행렬 (w[i][j]: i -> j 비용, 0이면 이동 불가)
    :return: 최소 비용
"""
def solve_tsp(n, w):

    INF = float('inf')
    # dp[visited_bitmask][current_city]
    # visited_bitmask: 방문한 도시들의 집합 (비트로 표현)
    # current_city: 현재 위치한 도시
    dp = [[None] * n for _ in range(1 << n)]

    def dfs(mask, cur):
        # 모든 도시를 방문했을 때 (mask가 11...11 이면)
        if mask == (1 << n) - 1:
            # 현재 도시에서 시작 도시(0번)로 돌아갈 수 있는지 확인
            if w[cur][0] == 0:
                return INF
            return w[cur][0]

        # 이미 계산한 적 있다면 메모이제이션 값 반환
        if dp[mask][cur] is not None:
            return dp[mask][cur]

        min_cost = INF
        
        # 다음 도시 탐색
        for next_city in range(n):
            # 아직 방문하지 않았고(비트가 꺼져있고), 길이 있다면
            if (mask & (1 << next_city)) == 0 and w[cur][next_city] != 0:
                cost = dfs(mask | (1 << next_city), next_city)
                if cost != INF:
                    min_cost = min(min_cost, cost + w[cur][next_city])
        
        dp[mask][cur] = min_cost
        return min_cost

    # 0번 도시에서 출발, 마스크 1(00...01) 상태로 시작
    result = dfs(1, 0)
    return result if result != INF else -1

if __name__ == "__main__":
    # 예제
    # 대칭 행렬일 필요는 없음
    N = 4
    W = [
        [0, 10, 15, 20],
        [5,  0,  9, 10],
        [6, 13,  0, 12],
        [8,  8,  9,  0]
    ]
    
    # 경로: 0 -> 1 -> 3 -> 2 -> 0
    # 비용: 10 + 10 + 9 + 6 = 35
    min_cost = solve_tsp(N, W)
    print(f"도시 개수: {N}")
    print(f"TSP 최소 비용: {min_cost}")
    
    assert min_cost == 35
