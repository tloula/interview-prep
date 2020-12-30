package interviews;

class SingleNumber {
    public static int singleNumber(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            boolean found = false;
            for (int j = 0; j < nums.length; j++) {
                if (nums[i] == nums[j] && i != j){
                    found = true;
                }
            }
            if (!found) {
                return nums[i];
            }
        }
        return -1;
    }
    public static void main(String[] args) throws Exception {
        int nums[] = {4, 1, 2, 1, 2};
        System.out.println(singleNumber(nums));
    }
}