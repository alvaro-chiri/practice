class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) == 1:
            return False
        elif s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False
        else:
            for i in s:
                if i == "(" or i == "{" or i =="[":
                    stack.append(i)
                elif i == ")" and "(" in stack:
                    if stack[-1] == "(":
                        stack.pop()
                elif i == "}" and "{" in stack:
                    if stack[-1] == "{":
                        stack.pop()
                elif i == "]" and "[" in stack:
                    if stack[-1] == "[":
                         stack.pop()
                else:
                    return False
        if stack == []:
            return True


                