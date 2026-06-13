from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        graph=defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited=set()
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        dfs(0)
        


        return len(visited) == n