"""
Question statement: 
Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be uniquely reconstructed from the array of sequences.

Unique reconstruction means that we need to find if originalSeq is the only sequence such that all sequences in the array are subsequences of it. 
"""

from collections import deque

class Solution:
    
    def solve(self, arr, seqs):
            
        order = []
        graph = {i: [] for i in arr}
        inDegrees = {i: 0 for i in arr}
        
        # print(inDegrees)
        
        for edges in seqs:
            for i in range(1, len(edges)):
                parent, child = edges[i-1], edges[i]
                # print((parent, child))
                graph[parent].append(child)
                inDegrees[child] += 1

        sources = deque()
        
        for key in graph:
            if inDegrees[key] == 0:
                sources.append(key)
            
        while sources:
            if len(sources) > 1:
                return False
            vertex = sources.popleft()
            order.append(vertex)
            for neighbor in graph[vertex]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    sources.append(neighbor)
        
        print(order)
        if len(order) != len(arr):
            return False
            
        return True
 
arr =[3, 1, 4, 2, 5] 
seqs = [[3,1,5], [1, 4, 2, 5]] 
# arr = [1, 13, 1, 24, 13, 24, 2, 2]

sol = Solution()
print(sol.solve(arr, seqs))
