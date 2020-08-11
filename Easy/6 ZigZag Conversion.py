class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        l = len(s)
        jump = 2 * numRows - 2
        row0 = [s[i] for i in range(0, l, jump)]
        for j in range(1, numRows - 1):
            rowj = [s[l] for l in sorted(list(range(j, l, jump))+list(range(jump-j, l, jump)))]
            row0 = row0 + rowj
        rownumRows = [s[i] for i in range(numRows-1, l, jump)]
        row0 = row0 + rownumRows
        return "".join(row0)


sol = Solution()
sol.convert(s="PAYPALISHIRING", numRows=3)
print(sol.convert(s="PAYPALISHIRING", numRows=3))
