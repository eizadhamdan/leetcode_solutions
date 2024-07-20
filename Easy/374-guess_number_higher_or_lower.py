# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

import random
class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n
        
        if guess(start) == 0:
            return start
        if guess(end) == 0:
            return end

        pick = (start + end) // 2
        
        ans = guess(pick)

        while True:
            if ans == 0:
                return pick
            elif ans == -1:
                end = pick
                pick = (start + end) // 2
                ans = guess(pick)
            else:
                start = pick
                pick = (start + end) // 2
                ans = guess(pick)