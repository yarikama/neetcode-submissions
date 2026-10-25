class MyHashMap:
    # open addressing
    _empty = object()
    _deleted = object()

    # params
    _factor = 0.5
    _not_found = -1

    def __init__(self, cap: int = 2):
        self.cap = cap

        self.keys = [self._empty] * self.cap
        self.vals = [0] * self.cap 

        self.size = 0 # real keys 
        self.used = 0 # real keys + deleted

    def _find(self, key: int) -> Tuple[bool, int]: # is_found, location
        i = hash(key) % self.cap
        tomb = self._not_found # set tomb for put

        while self.keys[i] is not self._empty:
            if self.keys[i] == key:
                return True, i

            if self.keys[i] is self._deleted and tomb == -1:
                tomb = i

            i = (i + 1) % self.cap

        return False, (tomb if tomb != self._not_found else i)

    def _resize(self) -> None:
        # record them for future use
        old_keys, old_vals = self.keys, self.vals

        # reset
        self.cap *= 2
        self.keys = [self._empty] * self.cap
        self.vals = [0] * self.cap
        self.used = 0
        self.size = 0

        # put them back
        for key, val in zip(old_keys, old_vals):
            if key is not self._empty and key is not self._deleted:
                self.put(key, val)

    def put(self, key: int, value: int) -> None:
        is_found, idx = self._find(key)

        if not is_found:
            self.size += 1
            if self.keys[idx] is self._empty:
                self.used += 1  

        self.vals[idx] = value
        self.keys[idx] = key
        
        if self.used >= self.cap * self._factor:
            self._resize()

    def get(self, key: int) -> int:
        is_found, idx = self._find(key)
        return self.vals[idx] if is_found else self._not_found

    def remove(self, key: int) -> None:
        is_found, idx = self._find(key)
        if is_found:
            self.size -= 1
            self.keys[idx] = self._deleted

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)