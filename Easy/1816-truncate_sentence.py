class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # sentence = list(s.split(' '))
        # ans = ""
        # for word in sentence[:k]:
        #     ans += word
        #     ans += ' '
        # ans = ans.rstrip(' ')
        # return ans

        words = s.split(' ')
        return " ".join(words[:k])