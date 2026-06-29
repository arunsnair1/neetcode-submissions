from collections import deque, defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {}

        for word in words:
            for ch in word:
                indegree[ch] = 0

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break

        qu = deque()

        for ch in indegree:
            if indegree[ch] == 0:
                qu.append(ch)

        ans = []

        while qu:
            node = qu.popleft()
            ans.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    qu.append(nei)

        if len(ans) != len(indegree):
            return ""

        return "".join(ans)