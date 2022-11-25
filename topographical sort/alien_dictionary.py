from collections import deque

class Solution:
    def findOrder(self,dict, N, K):
        # code here
        sortedOrder = []

        letters = set(''.join(dict))
        graph = {key: [] for key in letters}
        inDegrees = {key: 0 for key in letters}
        
        # build Graph
        for i in range(1, N):
            j = 0
            while j < min(len(dict[i]), len(dict[i-1])) and dict[i][j] == dict[i-1][j]:
                j += 1
            # print((i, dict[i-1][j], dict[i][j]))
            if j == min(len(dict[i]), len(dict[i-1])):
                continue
            graph[dict[i-1][j]].append(dict[i][j])
            inDegrees[dict[i][j]] += 1

        sources = deque()
        for key in inDegrees:
            if inDegrees[key] == 0:
                sources.append(key)

        while sources:
            curr = sources.popleft()
            sortedOrder.append(curr)
            for neighbor in graph[curr]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    sources.append(neighbor)
        # print(sortedOrder)
        if len(sortedOrder) != len(letters):
            return ""
        return sortedOrder

sol = Solution()
dict = ["caa","aaa","aab"]
print(sol.findOrder(dict, 3,3))
