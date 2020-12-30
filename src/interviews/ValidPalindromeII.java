package interviews;

public class ValidPalindromeII {
    public static boolean validPalindrome(String s) {
        boolean removed = false;
        for (int i = 0, j = s.length() - 1; i < j; i++, j--) {
            if (s.charAt(i) != s.charAt(j)) {
                if (!removed) {
                    if (s.charAt(i+1) == s.charAt(j)) {
                        removed = true;
                        ++i;
                    } else if (s.charAt(i) == s.charAt(j-1)) {
                        removed = true;
                        --j;
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }
        return true;
    }
    public static void main(String[] args) throws Exception {
        String s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga";
        System.out.println(validPalindrome(s));
    }
}