from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hash: Dict[str, List[Tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        elements = self.hash[key]

        if not elements:
            return ""

        L, R = 0, len(elements)-1

        if timestamp < elements[L][0]:
            return ""

        if elements[R][0] < timestamp:
            return elements[R][1]

        while L <= R:
            mid = (L + R) // 2
            if mid == len(elements)-1 or elements[mid][0] <= timestamp < elements[mid+1][0]:
                return elements[mid][1]
            elif elements[mid][0] > timestamp:
                R = mid - 1
            else:
                L = mid + 1

        return "" 

        
