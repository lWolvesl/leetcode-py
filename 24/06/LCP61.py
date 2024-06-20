from itertools import groupby, pairwise
from typing import List


class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        def getTrend(x: int, y: int) -> int:
            if x == y:
                return 0
            return -1 if x < y else 1

        ans = count = 0
        for i in range(1, len(temperatureA)):
            a = getTrend(temperatureA[i - 1], temperatureA[i])
            b = getTrend(temperatureB[i - 1], temperatureB[i])
            if a == b:
                count += 1
                ans = max(ans, count)
            else:
                count = 0
        return ans


# 一行搞定
class Solution:
    def temperatureTrend(self, A: List[int], B: List[int], cmp = lambda a, b: 1 if a < b else 0 if a == b else -1) -> int:
        return max((len([*g]) for tag, g in groupby(x == y for x, y in zip((cmp(a, b) for a, b in pairwise(A)), (cmp(a, b) for a, b in pairwise(B)))) if tag), default=0)
