"""
    Problem Statement: https://www.geeksforgeeks.org/minimum-number-deletions-make-sorted-sequence/

"""


class Solution:
	def minDeletions(self, arr, n):
	    
	    dp = [[-1 for _ in range(len(arr) + 1)] for _ in range(len(arr) + 1)]
	    # longest increasing subsequence
	    def recurse(i, j):
	        if j > len(arr) - 1:
	            return 0
            
            if dp[i][j] != - 1:
                return dp[i][j]
            
            total1, total2 = 0, 0
            if i == -1 or arr[j] > arr[i]:
                # take
                total1 = recurse(j, j+1) + 1
            
            # no take
            total2 = recurse(i, j+1)
            
            dp[i][j] = max(total1, total2)
	        return dp[i][j]
	        
	    lis_len = recurse(-1, 0)
        
        return len(arr) - lis_len
