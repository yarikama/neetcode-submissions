from typing import List

class MyHashMap[K, V]:
    _EMPTY, _DELETE = object(), object()
    _NOTFOUND = -1
    _FACTOR = 0.5

    def __init__(self, cap: int = 2):
        self.cap = cap
        self.keys: List[T] = [self._EMPTY] * self.cap
        self.vals: List[T] = [self._NOTFOUND] * self.cap

        self.size = 0 # real keys
        self.used = 0 # keys + deleted

    def _find[T](self, key: T) -> Tuple[bool, int]:
        i = hash(key) % self.cap
        tomb = self._NOTFOUND

        while self.keys[i] is not self._EMPTY:
            if self.keys[i] is self._DELETE and tomb == self._NOTFOUND:
                tomb = i

            elif self.keys[i] == key:
                return True, i

            i = (i + 1) % self.cap

        return (False, tomb if tomb != self._NOTFOUND else i)

    def _resize(self) -> None:
        old_keys, old_vals = self.keys, self.vals
        self.cap *= 2
        self.keys = [self._EMPTY] * self.cap
        self.vals = [self._NOTFOUND] * self.cap
        self.size = 0 
        self.used = 0 

        for k, v in zip(old_keys, old_vals):
            if k is not self._EMPTY and k is not self._DELETE:
                self.put(k, v)

    def put(self, key: int, value: int) -> None:
        is_found, index = self._find(key)
        if not is_found:
            if self.keys[index] is self._EMPTY:
                self.used += 1
            self.keys[index] = key
            self.size += 1
        self.vals[index] = value
        if self.used >= self.cap * self._FACTOR:
            self._resize()

    def get(self, key: int) -> T:
        is_found, index = self._find(key)        
        return self.vals[index] if is_found else -1

    def remove(self, key: int) -> None:
        is_found, index = self._find(key)
        if is_found:
            self.size -= 1
            self.keys[index] = self._DELETE
            self.vals[index] = self._NOTFOUND

# Your MyHashMap object will be instantiated and called as such:
# obj.put(key,value)
# obj = MyHashMap()
# param_2 = obj.get(key)
# obj.remove(key)