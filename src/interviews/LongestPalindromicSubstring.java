package interviews;

public class LongestPalindromicSubstring {
    public static String longestPalindrome(String s) {
        if (s == null || s.length() == 0 || s == "") return s;
        int[] longest = {0, 0};
        for (int i = 0; i < s.length(); i++) {
            int[] tmp = expandFromCenter(s, i);
            if (tmp[1] - tmp[0] > longest[1] - longest[0]) longest = tmp;
        }
        return s.substring(longest[0], ++longest[1]);
    }
    
    public static int[] expandFromCenter(String s, int index) {
        
        int i = index, j = index;
        if (index > 0 && s.charAt(index - 1) == s.charAt(index)) --i;
        else if (index < s.length()-1 && s.charAt(index + 1) == s.charAt(index)) ++j;
        
        for (; i >= 0 && j < s.length(); i--, j++) {
            if (s.charAt(i) != s.charAt(j)) return new int[] {++i, --j};
        }
        return new int[] {++i, --j};
    }
    public static void main(String[] args) throws Exception {
        String s = "aaaa";
        System.out.println(longestPalindrome(s));
    }
}