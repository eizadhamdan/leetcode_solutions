class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        
        # Precompute parity changes
        parity_changes = [0] * (n + 1)
        for i in range(1, n):
            parity_changes[i] = parity_changes[i-1] + (nums[i-1] % 2 != nums[i] % 2)
        
        # Process queries
        return [parity_changes[right] - parity_changes[left] == right - left for left, right in queries]
    