class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = -1
        for i in range(len(haystack)):
            if ans < 0:
                if haystack[i:len(needle)+i] == needle:
                    ans = i
        return ans
                