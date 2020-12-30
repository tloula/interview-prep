package interviews;

import java.util.List;
import java.util.ArrayList;

public class SelfDividingNumbers {
    public static List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> list = new ArrayList<>();
        for (int i = left; i <= right; i++) {
            if (i == 0) continue;
            boolean div = true;
            int digit = 0;
            for (char c : Integer.toString(i).toCharArray()) {
                digit = c - '0';
                if (i%digit != 0) div = false;
            }
            if (div) list.add(digit);
        }
        return list;
    }
    public static void main(String[] args) throws Exception {
        System.out.println(selfDividingNumbers(1, 22));
    }
}