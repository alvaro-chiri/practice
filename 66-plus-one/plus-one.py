class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits]
        number = int("".join(s))
        number += 1
        lst = [int(i) for i in str(number)]

        return lst