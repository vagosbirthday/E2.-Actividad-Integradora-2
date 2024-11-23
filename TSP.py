
# Codigo sacado de https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-in-python/

# Modificado y adaptado por: Kirill Makienko


class TSP:
    def __init__(self, n, dist):
        self.n = n
        self.dist = dist
        # Adjust memo size to match dimensions
        self.memo = [[-1]*(1 << (n+1)) for _ in range(n+1)]
        
    def solve(self):
        # Create initial mask with all cities (1-based indexing)
        ans = 10**9
        for i in range(1, self.n+1):
            # try to go from node 1 visiting all nodes in between to i
            # then return from i taking the shortest route to 1
            ans = min(ans, self.fun(i, (1 << (self.n+1))-1) + self.dist[i][1])
        
        return ans
    
    def fun(self, i, mask):
        # base case
        # if only ith bit and 1st bit is set in our mask,
        # it implies we have visited all other nodes already
        if mask == ((1 << i) | 3):
            return self.dist[1][i]

        # memoization
        if self.memo[i][mask] != -1:
            return self.memo[i][mask]

        res = 10**9  # result of this sub-problem

        # we have to travel all nodes j in mask and end the path at ith node
        # so for every node j in mask, recursively calculate cost of
        # travelling all nodes in mask
        # except i and then travel back from node j to node i taking
        # the shortest path take the minimum of all possible j nodes
        for j in range(1, self.n):
            if (mask & (1 << j)) != 0 and j != i and j != 1:
                res = min(res, self.fun(j, mask & (~(1 << i))) + self.dist[j][i])
        self.memo[i][mask] = res  # storing the minimum value
        return res
