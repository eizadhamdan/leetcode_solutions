class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        
        single_list: list[int] = []
        for num, freq in frequency.items():
            if freq == 1:
                single_list.append(num)
        
        return single_list
    