class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        splitted_v1 = list(map(int, version1.split('.')))
        splitted_v2 = list(map(int, version2.split('.')))
        
        max_length = max(len(splitted_v1), len(splitted_v2))
        splitted_v1 += [0] * (max_length - len(splitted_v1))
        splitted_v2 += [0] * (max_length - len(splitted_v2))
        
        for i in range(max_length):
            if splitted_v1[i] > splitted_v2[i]:
                return 1
            elif splitted_v1[i] < splitted_v2[i]:
                return -1
        
        return 0