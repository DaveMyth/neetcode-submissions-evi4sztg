class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        curRecord = self.timeMap[key] if key in self.timeMap else []
        curRecord.append([value, timestamp])
        self.timeMap[key] = curRecord

    def get(self, key: str, timestamp: int) -> str:
        curRecord = self.timeMap[key] if key in self.timeMap else None

        if not curRecord:
            return ""

        curRecord.sort(key = lambda x: x[1], reverse=True)
        ctr = 0
        while ctr < len(curRecord) and curRecord[ctr][1] > timestamp:
            ctr += 1

        if ctr == len(curRecord):
            return ""
        return curRecord[ctr][0]
