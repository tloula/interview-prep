package interviews;

import java.util.*;

public class ThreeSum {
    public static List<List<Integer>> threeSum(int[] nums) {
        
        List<List<Integer>> sums = new ArrayList<List<Integer>>();
        if (nums == null || nums.length == 0) return sums;
        
        HashSet<Integer> set = new HashSet<>();
        int length = nums.length;
        for (int i = 0, j = 0; j < nums.length; j++) {
            if (!set.contains(nums[j])) {
                set.add(nums[j]);
                nums[i++] = nums[j];
            }
            length = i;
        }
        
        for (int i = 0; i < length; i++) {
            for (int j = i+1; j < length; j++) {
                for (int k = j+1; k < length; k++) {
                    if (nums[i] + nums[j] + nums[k] == 0) sums.add(Arrays.asList(nums[i], nums[j], nums[k]));
                }
            }
        }
        return sums;
    }
    public static void main(String[] args) throws Exception {
        int nums[] = {-1,0,1,2,-1,-4};
        System.out.println(threeSum(nums));
    }
}