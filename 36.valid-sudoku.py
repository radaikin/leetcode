#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        res = []

        for i, row in enumerate(board):
            for j, element in enumerate(row):
                if element != ".":
                    if (i, element) in res or \
                       (element, j) in res or \
                       (i//3, j//3, element) in res:
                        return False
                    res.append((i, element))
                    res.append((element, j))
                    res.append((i//3, j//3, element))
        return len(res) == len(set(res))
# @lc code=end

# debug
# Solution().isValidSudoku(board =
# [["7",".",".", ".","4",".", ".",".","."],
#  [".",".",".", "8","6","5", ".",".","."],
#  [".","1",".", "2",".",".", ".",".","."],

#  [".",".",".", ".",".","9", ".",".","."],
#  [".",".",".", ".","5",".", "5",".","."],
#  [".",".",".", ".",".",".", ".",".","."],

#  [".",".",".", ".",".",".", "2",".","."],
#  [".",".",".", ".",".",".", ".",".","."],
#  [".",".",".", ".",".",".", ".",".","."]])
