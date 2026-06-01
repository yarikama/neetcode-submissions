class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            for c in string:
                res += (str(ord(c)) + ",")
            res += " "
        return res


    def decode(self, s: str) -> List[str]:
        encoded_words = [word for word in s.split(" ")]
        encoded_words = list(map(lambda x: x.split(","), encoded_words))
        encoded_words.pop()

        result = []
        for word in encoded_words:
            chars = [chr(int(c)) for c in word if c]
            result.append("".join(chars))

        return result

