
"""
    Unbounded Knapsack Problem No. 5 from Educative io DP course
    Problem Statement:
       https://www.geeksforgeeks.org/maximum-number-segments-lengths-b-c/

"""

import math

def solution(N, a, b, c):
    
    # stores the max cuts possible for ith size of ribbon
    dp = [-1 for i in range(N+1)]
    def recurse_find(N, a, b, c):
        if N == 0:
            return 0
        
        # if at the end you couldnt reach 0 then this whole path should be rejected
        if N < 0:
            return -math.inf
        
        if dp[N] == -1:
            max_cuts = 0
            # at every step you can either cut a size or b size or c size
            max_cuts = max(recurse_find(N-a, a, b, c), recurse_find(N-b, a, b, c), recurse_find(N-c, a, b, c)) + 1
            dp[N] = max_cuts
        
        return dp[N]

    return recurse_find(N, a, b, c)



if __name__ == '__main__':
    N, a, b, c = (7, 17), (5, 2), (2, 1), (5, 3)  
    
    #for i range(2):
    i = 1
    sol = solution(N[i], a[i], b[i], c[i]) 
    print(sol)

    #input()



