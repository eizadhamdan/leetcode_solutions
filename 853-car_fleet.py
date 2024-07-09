class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair):
            time = (target - p) / s
            while stack and time >= stack[-1]:
                # a previous car reaches the target before or at same time.
                # thus they form a fleet, pop the faster car
                stack.pop()
            stack.append(time)
        return len(stack)
