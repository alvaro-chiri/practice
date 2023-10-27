class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        reverseS = s[::-1]

        if s == reverseS:
            return True
        else:
            return False
            