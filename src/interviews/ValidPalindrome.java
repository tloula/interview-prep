package interviews;

public class ValidPalindrome {
    public static boolean isPalindrome(String s) {
        s = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
        for (int i = 0, j = s.length()-1; i < j; i++, j--) {
            if (s.charAt(i) != s.charAt(j)) return false;
        }
        return true;
    }
    public static void main(String[] args) throws Exception {
        String s = "A man, a plan, a canal: Panama";
        System.out.println(isPalindrome(s));
    }
}