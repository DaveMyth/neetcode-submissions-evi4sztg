class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = {}
        self.keysCache = collections.deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.keysCache.remove(key)
            self.keysCache.append(key)
            return self.hashMap[key]
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.hashMap:
            self.keysCache.remove(key)
        else:
            self.capacity -= 1
        self.keysCache.append(key)
        self.hashMap[key] = value

        if self.capacity < 0:
            self.hashMap.pop(self.keysCache.popleft())
            self.capacity += 1