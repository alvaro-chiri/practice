class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0

        converter = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        i = 0

        while i < len(s):
            if i + 1 < len(s) and converter[s[i]] < converter[s[i+1]]:
                result += converter[s[i+1]] - converter[s[i]]
                i += 2
            else:
                result += converter[s[i]]
                i += 1

        return result