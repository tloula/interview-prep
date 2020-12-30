class Solution:
    def exist(self, board, word):
        def dfs(pos, coords):
            coords.add(pos)
            if len(coords) == len(word): return True
            x, y = pos
            next_letter = word[len(coords)]
            found = False
            if x > 0 and (x-1, y) not in coords and board[y][x-1] == next_letter: found = found or dfs((x-1, y), coords.copy())
            if x < len(board[0]) - 1 and (x+1, y) not in coords and board[y][x+1] == next_letter: found = found or dfs((x+1, y), coords.copy())
            if y > 0 and (x, y-1) not in coords and board[y-1][x] == next_letter: found = found or dfs((x, y-1), coords.copy())
            if y < len(board) - 1 and (x, y+1) not in coords and board[y+1][x] == next_letter: found = found or dfs((x, y+1), coords.copy())
            return found

        return any([dfs((i, j), set()) for j, row in enumerate(board) for i, letter in enumerate(row) if letter == word[0]])
    
s = Solution()
#print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))
