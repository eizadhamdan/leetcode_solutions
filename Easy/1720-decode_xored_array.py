class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded_array = []
        decoded_array.append(first)
        for i in range(len(encoded)):
            new_num = encoded[i] ^ first
            decoded_array.append(new_num)
            first = new_num
        return decoded_array
    