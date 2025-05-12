import heapq
from collections import defaultdict

class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        graph = defaultdict(list)
        for road in roads:
            u, v, time = road
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        min_time = [float('inf')] * n
        ways = [0] * n
        min_time[0] = 0
        ways[0] = 1
        
        heap = []
        heapq.heappush(heap, (0, 0))
        
        while heap:
            current_time, u = heapq.heappop(heap)
            
            if current_time > min_time[u]:
                continue
                
            for neighbor in graph[u]:
                v, time = neighbor
                if min_time[v] > current_time + time:
                    min_time[v] = current_time + time
                    ways[v] = ways[u]
                    heapq.heappush(heap, (min_time[v], v))
                elif min_time[v] == current_time + time:
                    ways[v] = (ways[v] + ways[u]) % MOD
        
        return ways[n-1] % MOD
    

def main():
    sol = Solution()
    n1 = 7
    roads1 = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    print(f"{sol.countPaths(n1, roads1)}") # 4
    n2 = 2
    roads2 = [[1,0,10]]
    print(f"{sol.countPaths(n2, roads2)}") # 1
    n3 = 4
    roads3 = [[0,1,1],[1,2,1],[2,3,1]]
    print(f"linear {sol.countPaths(n3, roads3)}") # 1
    n4 = 4
    roads4 = [[0,1,1],[0,2,2],[1,3,2],[2,3,1]]
    print(f"múltiplos caminhos {sol.countPaths(n4, roads4)}") # 2
    n5 = 3
    roads5 = [[0,1,5],[1,2,5],[0,2,15]]
    print(f"caminho direto mais longo {sol.countPaths(n5, roads5)}") # 1 

if __name__ == "__main__":
    main()
    
