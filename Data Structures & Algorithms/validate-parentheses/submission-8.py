class Solution:
    def isValid(self, s: str) -> bool:
        pre_set = "({["
        stack = []

        for br in s:
            if br in pre_set:
                stack.append(br)
            elif stack and ((br == ')' and stack[-1] == '(') or (br == '}' and stack[-1] == '{') or (br == ']' and stack[-1] == '[')):
                stack.pop()
            else:
                return False

        return not bool(stack)

