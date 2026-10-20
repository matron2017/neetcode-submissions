class TimeMap:

    def __init__(self):
        self.store = {} # key "alice" : [2: angry]  
        # key alice: value happy
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append(tuple([timestamp, value]))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]
        l = 0
        n = len(values)
        r = n - 1
        m = (l+r) // 2
        best_index = None
        while r >= l:
            number = values[m][0]
            if number != timestamp:
                if number <= timestamp:
                    best_index = m
                    l = m + 1
                    m = (l+r) // 2
                else:
                    r = m - 1
                    m = (l+r) // 2
            else:
                return values[m][1]

        if best_index == None:
            return ""
        return values[best_index][1]
        
