class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        if n == 1:
            return s
        encrypted_text = ""
        for i in range(n):
            encrypted_text += s[(i + k) % n]
        return encrypted_text
    