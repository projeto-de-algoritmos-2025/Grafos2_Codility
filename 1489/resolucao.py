class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """

        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return False
                self.parent[py] = px
                return True

        indexed_edges = [edge + [i] for i, edge in enumerate(edges)]
        indexed_edges.sort(key=lambda x: x[2])

        def kruskal(n, edges, include=None, exclude=None):
            uf = UnionFind(n)
            weight = 0

            if include is not None:
                u, v, w, _ = include
                if uf.union(u, v):
                    weight += w

            for u, v, w, idx in edges:
                if idx == exclude:
                    continue
                if uf.union(u, v):
                    weight += w

            root = uf.find(0)
            for i in range(1, n):
                if uf.find(i) != root:
                    return float('inf')
            return weight

        min_cost = kruskal(n, indexed_edges)

        critical = []
        pseudo_critical = []

        for u, v, w, i in indexed_edges:
            if kruskal(n, indexed_edges, exclude=i) > min_cost:
                critical.append(i)
            elif kruskal(n, indexed_edges, include=[u, v, w, i]) == min_cost:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]
