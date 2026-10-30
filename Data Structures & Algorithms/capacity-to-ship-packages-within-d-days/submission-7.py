class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)

        def able_to_finish(cap: int, days: int) -> bool:
            curr_cap, curr_day = 0, 1 

            for w in weights:
                if w > cap:
                    return False

                if cap - curr_cap >= w:
                    curr_cap += w
                else:
                    curr_cap = w
                    curr_day += 1

                # print(f"\tday: {curr_day}, cap: {curr_cap}")

                if curr_day > days:
                    return False

            return True



        L, R = min(weights), total
        if L > R:
            L, R = R, L

        while L <= R:
            mid = (L + R) // 2

            if res := able_to_finish(mid, days):
                R = mid - 1

            else:
                L = mid + 1

            # print(f"Able to finish in cap {mid}: {res}")

        return L