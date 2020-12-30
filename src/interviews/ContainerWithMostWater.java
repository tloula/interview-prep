package interviews;

public class ContainerWithMostWater {
    // Brute Force
    /*public static int maxArea(int[] height) {
        int maxArea = 0;
        for (int i = 0; i < height.length; i++)
            for (int j = i+1; j < height.length; j++)
                maxArea = Math.max(maxArea, (j - i) * Math.min(height[i], height[j]));
        return maxArea;
    }*/
    
    // Two Pointer
    public static int maxArea(int[] height) {
        int maxArea = 0;
        for (int i = 0, j = height.length - 1; i < j;) {
            maxArea = Math.max(maxArea, (j - i) * Math.min(height[i], height[j]));
            if (height[i] > height[j]) --j;
            else ++i;
        }
        return maxArea;
    }
    public static void main(String[] args) throws Exception {
        int nums[] = {1,8,6,2,5,4,8,3,7};
        System.out.println(maxArea(nums));
    }
}