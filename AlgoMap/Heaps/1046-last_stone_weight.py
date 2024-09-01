import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # def remove_largest():
        #     largest_i = stones.index(max(stones))
        #     return stones.pop(largest_i)

        # while len(stones) > 1:
        #     y = remove_largest()
        #     x = remove_largest()

        #     if x != y:
        #         stones.append(y - x)

        # return stones[0] if stones else 0

        # using a max-heap
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if y != x:
                heapq.heappush(stones, y-x)

        return -heapq.heappop(stones) if stones else 0
    