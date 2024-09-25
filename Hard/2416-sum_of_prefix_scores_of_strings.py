class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
    
    def get_score(self, word):
        node = self.root
        score = 0
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            score += node.count
        return score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # len_words = len(words)
        # ans = []
        # for word in words:
        #     prefixes = []
        #     for i in range(1, len(word)):
        #         prefixes.append(word[0:i])
        #     prefixes.append(word)
        #     count = 0
        #     for prefix in prefixes:
        #         for index in range(len_words):
        #             if words[index].startswith(prefix):
        #                 count += 1
        #     ans.append(count)

        # return ans

        trie = Trie()
        for word in words:
            trie.insert(word)
        
        return [trie.get_score(word) for word in words]
    