class Solution:
    def decodeString(self, s: str) -> str:
        nums = []
        prefix_stack = [""]

        is_last_num = False
        
        for ch in s:
            if "0" <= ch <= "9":
                if is_last_num: 
                    nums[-1] = nums[-1] * 10 + int(ch)
                else:
                    nums.append(int(ch))
                is_last_num = True

            else:
                is_last_num = False

                if ch == "[":
                    prefix_stack.append("")
                
                elif ch == "]":
                    suffix = prefix_stack.pop()
                    times = nums.pop()
                    prefix_stack[-1] += (times * suffix)

                else:
                    prefix_stack[-1] += ch


        return prefix_stack[-1]
