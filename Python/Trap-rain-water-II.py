import heapq
class Solution:
    #def trapRainWater(self, heightMap: List[List[int]]) -> int:
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []

        # Push boundary cells into the min heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        total_volume = 0

        while heap:
            height, x, y = heapq.heappop(heap)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    total_volume += max(0, height - heightMap[nx][ny])
                    heapq.heappush(heap, (max(heightMap[nx][ny], height), nx, ny))

        return total_volume