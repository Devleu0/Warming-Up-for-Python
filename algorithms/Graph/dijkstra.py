"""Dijkstra 최단 경로 (우선순위 큐, O(E log V))."""
import heapq
import sys

INF = int(1e9)


def dijkstra(graph, start):
    """graph[u] = [(v, cost), ...]. start 에서 각 노드까지의 최단 거리 리스트를 반환."""
    distance = [INF] * len(graph)
    distance[start] = 0
    q = [(0, start)]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:  # 이미 처리된 노드
            continue
        for nxt, w in graph[now]:
            cost = dist + w
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))
    return distance


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    distance = dijkstra(graph, start)
    for d in distance[1:]:
        print("INFINITY" if d == INF else d)


if __name__ == "__main__":
    main()

'''
[Input Example 1]
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
[Output Example 1]
0
2
3
7
INFINITY
'''
