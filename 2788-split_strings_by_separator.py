class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            to_append = word.split(separator)
            for splitted_word in to_append:
                if splitted_word == "":
                    continue
                ans.append(splitted_word)
        return ans