class MyHashSet:
    _empty = object()
    _deleted = object()
    _not_found = -1
    _factor = 0.5

    def __init__(self, cap: int = 100):
        self.cap = cap
        self.keys = [self._empty] * self.cap
        self.used = 0
        self.size = 0

    def _find(self, key: int) -> Tuple[bool, int]:
        i = hash(key) % self.cap
        tomb = -1

        while self.keys[i] != self._empty:
            if self.keys[i] == key:
                return True, i

            if self.keys[i] is self._deleted and tomb == self._not_found:
                tomb = i

            i = (i + 1) % self.cap

        return False, (tomb if tomb != self._not_found else i) # if we found a tomb -> pass back

    def add(self, key: int) -> None:
        is_found, idx = self._find(key)
        if not is_found:
            if self.keys[idx] is self._deleted:
                self.size += 1

            self.keys[idx] = key
            self.used += 1

        if self.used >= self.cap * self._factor:
            self._resize()

    def _resize(self) -> None:
        old_keys = self.keys
        self.cap *= 2
        self.keys = [self._empty] * self.cap
        self.used = 0
        self.size = 0

        for key in old_keys:
            if key is not self._empty:
                self.add(key)

    def remove(self, key: int) -> None:
        is_found, idx = self._find(key)
        if is_found:
            self.keys[idx] = self._deleted
            self.size -= 1

    def contains(self, key: int) -> bool:
        is_found, _ = self._find(key)
        return is_found


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)