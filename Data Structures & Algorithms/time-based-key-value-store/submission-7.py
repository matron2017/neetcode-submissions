from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.timemap[key]

        n = len(values)
        l = 0
        r = n - 1
        res = ""
        while l <= r:
            m = (l+r) // 2

            if values[m][1] < timestamp:
                res = values[m][0]
                l = m + 1
            elif values[m][1] > timestamp:
                r = m - 1
            else: 
                return values[m][0]
        
        return res
            

                

        