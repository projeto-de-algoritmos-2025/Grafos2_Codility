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
    
