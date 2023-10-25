class Solution:
    def mySqrt(self, x: int) -> int:
        s = 0
        e = x
        while s <= e:
            mid = (s+e) // 2
            if mid * mid > x:
                e = mid - 1
            elif mid*mid < x:
                s = mid + 1
            else:
                return mid
        return e
