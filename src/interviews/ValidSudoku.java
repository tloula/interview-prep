package interviews;

import java.util.HashSet;

class ValidSudoku {
    public static boolean isValidSudoku(char[][] board) {
        
        HashSet<Integer> row = new HashSet<>();
        HashSet<Integer> col = new HashSet<>();
        HashSet<Integer> box1 = new HashSet<>();
        HashSet<Integer> box2 = new HashSet<>();
        HashSet<Integer> box3 = new HashSet<>();
        
        for (int i = 0; i < 9; i++) {
            
            if(i != 0 && i%3 == 0) {
                box1.clear();
                box2.clear();
                box3.clear();
            }
            
            for (int j = 0; j < 9; j++) {
                if(board[i][j] != '.' && !row.add(board[i][j] - 48)) return false;
                if(board[j][i] != '.' && !col.add(board[j][i] - 48)) return false;
                
                if (board[i][j] != '.') {
                    if(j < 3            && !box1.add(board[i][j] - 48)) return false;
                    if(j > 2 && j < 6   && !box2.add(board[i][j] - 48)) return false;
                    if(j > 5            && !box3.add(board[i][j] - 48)) return false;
                }
            }
            
            row.clear();
            col.clear();
        }
        
        return true;
        
    }
    public static void main(String[] args) throws Exception {
        char nums[][] = {
            {'5','3','.','.','7','.','.','.','.'},
            {'6','.','.','1','9','5','.','.','.'},
            {'.','9','8','.','.','.','.','6','.'},
            {'8','.','.','.','6','.','.','.','3'},
            {'4','.','.','8','.','3','.','.','1'},
            {'7','.','.','.','2','.','.','.','6'},
            {'.','6','.','.','.','.','2','8','.'},
            {'.','.','.','4','1','9','.','.','5'},
            {'.','.','.','.','8','.','.','7','9'}
          };
        System.out.println(isValidSudoku(nums));
    }
}