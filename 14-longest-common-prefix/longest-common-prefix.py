class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs)
        first = sorted_strs[0]
        last = sorted_strs[-1]
        result = ''
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return result
            else:
                result += first[i]
        return result
