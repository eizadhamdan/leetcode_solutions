class Solution:
    def finalString(self, s: str) -> str:
        answer_string = ""

        for char in s:
            if char != 'i':
                answer_string += char
            else:
                answer_string = answer_string[::-1]

        return answer_string
    