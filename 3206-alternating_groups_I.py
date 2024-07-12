class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        groups = 0
        n = len(colors)
        for i in range(1, n - 1):
            if (colors[i] != colors[i-1]) and (colors[i] != colors[i+1]):
                groups += 1
        if (colors[n-1] != colors[0]) and (colors[0] != colors[1]):
            groups += 1
        if (colors[n-2] != colors[n-1]) and (colors[n-1] != colors[0]):
            groups += 1
        return groups