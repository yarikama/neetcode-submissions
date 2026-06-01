class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.digits = digits

        self.d_c_map = {}
        self.d_c_map['2'] = "abc"
        self.d_c_map['3'] = "def"
        self.d_c_map['4'] = "ghi"
        self.d_c_map['5'] = "jkl"
        self.d_c_map['6'] = "mno"
        self.d_c_map['7'] = "pqrs"
        self.d_c_map['8'] = "tuv"
        self.d_c_map['9'] = "wxyz"

        self.result = []
        self.helper(0, "")
        return self.result

    def helper(self, idx: int, comb: str) -> None:
        if len(comb) == len(self.digits):
            self.result.append(comb)
            return 

        if idx == len(self.digits):
            return

        for char in self.d_c_map[self.digits[idx]]:
            self.helper(idx+1, comb+char)
            self.helper(idx+1, comb)
