class MyHashMap:
    _EMPTY, _DELETE = object(), object()
    _FACTOR = 0.5

    def __init__(self, cap = 2):
        self.cap = cap
        self.keys = [self._EMPTY] * self.cap
        self.vals = [-1] * self.cap

        self.size = 0 # key
        self.used = 0 # key + deleted

    def put(self, key: int, value: int) -> None:
        i, found = self._find(key)
        if not found:
            if self.keys[i] is self._EMPTY:
                self.used += 1
            self.size += 1
            self.keys[i] = key
        self.vals[i] = value

        if self.used > self.cap * self._FACTOR:
            self._resize(self.cap * 2)
        

    def _find(self, key: int) -> Tuple[int, bool]:
        i = hash(key) % self.cap
        tomb = -1
        while self.keys[i] is not self._EMPTY:
            if self.keys[i] == key:
                return i, True
            if self.keys[i] is self._DELETE and tomb == -1:
                tomb = i
            i = (i + 1) % self.cap
        return (tomb if tomb != -1 else i, False)

    def get(self, key: int) -> int:
        i, found = self._find(key)
        return self.vals[i] if found else -1

    def remove(self, key: int) -> None:
        i, found = self._find(key)
        if found:
            self.keys[i] = self._DELETE
            self.size -= 1
        
    def _resize(self, new_cap: int) -> None:
        old_keys, old_vals = self.keys, self.vals
        self.cap = new_cap
        self.keys = [self._EMPTY] * new_cap
        self.vals = [0] * new_cap
        self.size = self.used = 0
        for k, v in zip(old_keys, old_vals):
            if k not in (self._EMPTY, self._DELETE) :
                self.put(k, v)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)