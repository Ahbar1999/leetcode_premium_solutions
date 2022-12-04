"Problem link: https://www.geeksforgeeks.org/cutting-a-rod-dp-13/"

import math
class Solution:
    def cutRod(self, price, n): 
        dp = [-1 for x in range(n + 1)]
        def search_recursively(price, n):
            # print(n)
            if n <= 0:
                return 0
            
            if dp[n] == -1:
                max_price = -math.inf
                for i in range(n):
                    # prices.append(search_recursively(price, n-i-1) + prices[i])
                    max_price = max(max_price, (search_recursively(price, n-i-1) + price[i]))
                    dp[n] = max_price
            
            return dp[n]
        
        return search_recursively(price, n)


if __name__ == '__main__':
    #ex
    price = [3, 5, 8, 9, 10, 17, 17, 20]
    n = 8
    sol = Solution().cutRod(price, n)
    print("Max price possible for the rods", sol)




