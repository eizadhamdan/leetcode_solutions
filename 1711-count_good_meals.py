class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ans = 0
        frequency = defaultdict(int)

        # Note that the number of powers of 2 is at most 21 so this turns the problem to a classic find the number of pairs that sum to a certain value but for 21 values
        for x in deliciousness:
            for k in range(22):
                ans += frequency[2 ** k - x]
            frequency[x] += 1
        return ans % (10 ** 9 + 7)