class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        #To maximize the enjoyment, serve dishes with higher satisfaction later in the sequence
        
        satisfaction.sort(reverse=True)
        
        max_enjoyment = 0
        current_sum = 0
        
        for s in satisfaction:
            current_sum += s
            if current_sum > 0:
                max_enjoyment += current_sum
            else:
                break
        
        return max_enjoyment