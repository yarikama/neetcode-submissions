class Solution:
    def carFleet(
        self, target: int, position: List[int], speed: List[int]
    ) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort()
        
        stack = [(-1, float('inf'))]
        for p1, s1 in cars:
            if p1 > target:
                break

            if stack and stack[-1][1] > s1:
                print(f"position: {p1}, speed: {s1}")
                print(f"can: {(p1 - stack[-1][0]) / (stack[-1][1] - s1)} <= {(target - p1) / s1}")
                while stack and stack[-1][1] > s1 and (p1 - stack[-1][0]) / (stack[-1][1] - s1) <= (target - p1) / s1:
                    stack.pop()
                else:
                    stack.append((p1, s1))
            else:
                stack.append((p1, s1))

        return len(stack)

        