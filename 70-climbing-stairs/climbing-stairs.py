class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        
        arr = [1,1]
        for i in range(2, n+1):
            temp = arr[i-1] + arr[i-2]
            arr.append(temp)
        return arr[n]