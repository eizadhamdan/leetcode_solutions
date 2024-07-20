class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        curr = nums[0]
        res = curr
        while left < n and right < n:
            # Increase the window. 
            # This is done so long as we do not encounter 
            # a 0 value, or exceed the array size, 
            # or left ptr==right ptr.
            
            if (right + 1 < n) and (curr * nums[right+1] != 0 or left == right):
                right += 1
                curr *= nums[right]

            # Shrink the window if the conditions to increase the window fail.
            else:
                if nums[left] != 0:
                    curr /= nums[left]
                else:
                    curr = sum(nums[i] for i in range(left, right+1))
                left += 1

            # Compare current window against prev best.
            # Protect this result against a final execution of this loop, should
            # the last element in the array be used (potentially leading a 
            # pointer out of bounds)
            
            if left <= right <= n:
                res = max(int(curr), res)

        return res 



        # Alternate Approach: Brute Force
        # --> checking all possible subarrays
        # --> time: O(n**2), space: O(1)
        # n = len(nums)
        # res = float('-inf')
        # for i in range(n):
        #     totalSum = nums[i]
        #     for j in range(i+1, n):
        #         totalSum *= nums[j]
        #         res = max(totalSum, res)
        # return res