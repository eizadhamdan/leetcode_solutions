class Solution:
    def isHappy(self, n: int) -> bool:
        # # to keep track of the cycles
        # seen = set()
        # curr = str(n)

        # while curr not in seen:
        #     seen.add(curr)
        #     digits_sum = 0
        #     for digit in curr:
        #         digit = int(digit)
        #         digits_sum += digit ** 2

        #     if digits_sum == 1:
        #         return True
        #     curr = str(digits_sum)

        # return False

        """alternative solution"""
        def get_next(num):
            return sum(int(x) ** 2 for x in str(num))

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1
        