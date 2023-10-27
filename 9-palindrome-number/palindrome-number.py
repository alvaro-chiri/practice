class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = False
        s = str(x)
        reverseS = s[::-1]

        for i in range(len(s)):
            if s[i] != reverseS[i]:
                return False
            else:
                ans = True

        return ans
            