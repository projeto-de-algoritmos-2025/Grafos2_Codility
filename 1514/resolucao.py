import heapq
from collections import defaultdict

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """

        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            prob = succProb[i]
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        max_heap = [(-1.0, start_node)]
        visited = [False] * n

        while max_heap:
            curr_prob, node = heapq.heappop(max_heap)
            curr_prob = -curr_prob  

            if node == end_node:
                return curr_prob

            if visited[node]:
                continue
            visited[node] = True

            for neighbor, edge_prob in graph[node]:
                if not visited[neighbor]:
                    heapq.heappush(max_heap, (-(curr_prob * edge_prob), neighbor))

        return 0.0  
