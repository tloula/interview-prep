package interviews;

import java.util.Arrays;

class MaximumProductOfThreeNumbers {
    public static int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        int product = 1;
        for (int i = nums.length - 1; i > nums.length - 4; i--) {
            product *= nums[i];
        }
        return product;
    }
    public static void main(String[] args) throws Exception {
        int nums[] = {-1, -2, -3};
        System.out.println(maximumProduct(nums));
    }
}