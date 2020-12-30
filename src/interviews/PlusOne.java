package interviews;

class PlusOne {
    public static int[] plusOne(int[] digits) {
        
        String s = "";
        for (int i : digits) {
            s += Integer.toString(i);
        }
        
        long i = Long.parseLong(s);
        ++i;
        
        s = Long.toString(i);
        
        int[] n = new int[s.length()];
        
        for (int j = 0; j < s.length(); j++){
            n[j] = s.charAt(j)-48;
        }
        
        return n;
    }

    public static void main(String[] args) throws Exception {
        int nums[] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
        System.out.println(plusOne(nums));
    }
}