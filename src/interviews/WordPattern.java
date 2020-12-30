package interviews;

import java.util.HashMap;

public class WordPattern {
    public static boolean wordPattern(String pattern, String str) {

        int a = pattern.length();
        int b = str.length();
        int c = str.replaceAll(" ", "").length();


        if (pattern.length() != str.length() - str.replaceAll(" ", "").length()+1) return false;
        


        HashMap<Character, String> map = new HashMap<>();
        String[] strings = str.split("\\s+");
        
        for (int i = 0; i < pattern.length(); i++) {
            char key = pattern.charAt(i);
            String value = strings[i];
            
            if (map.containsValue(value) && !map.containsKey(key)) return false;
            if (map.containsKey(key) && !map.get(key).equals(value)) {
                return false;
            } else {
                map.put(key, value);
            }
        }
        return true;
    }
    public static void main(String[] args) throws Exception {
        String pattern = "abba";
        String s = "dog dog dog dog";
        System.out.println(wordPattern(pattern, s));
    }
}