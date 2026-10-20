class TimeMap:

    def __init__(self):
        self.store = {} # key : list[(emo,timestamp)]
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]
        l = 0
        n = len(values)
        r = n - 1
        m = (l+r) // 2
        timestamp_prev = ""
        while r >= l:
            value_m, time_m = values[m]
            if time_m <= timestamp:
                timestamp_prev = value_m
                l = m + 1
                m = (l+r) // 2
            else:
                r = m - 1
                m = (l+r) // 2
        return timestamp_prev
        
