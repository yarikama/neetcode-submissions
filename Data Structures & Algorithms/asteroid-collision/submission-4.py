class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        def ops(a: int) -> None:
            if not stack:
                stack.append(a)
                return

            if a < 0 and stack[-1] > 0:
                if abs(a) < abs(stack[-1]):
                    return

                if abs(a) == abs(stack[-1]):
                    stack.pop()
                    return

                stack.pop()
                return ops(a)

            stack.append(a)

        for a in asteroids:
            ops(a)

        return stack


