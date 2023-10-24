class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for d in range(len(digits)-1, -1, -1):
            if digits[d] == 9:
                digits[d] = 0
            else:
                digits[d] = digits[d] + 1
                return digits
        return [1] + digits