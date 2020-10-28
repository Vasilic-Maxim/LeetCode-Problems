class Solution {
    public List<String> summaryRanges(int[] nums) {
        int n = nums.length;
        List<String> result = new LinkedList<>();
        if (n < 1) return result;

        int start = 0;
        for (int end = 1; end < nums.length; end++) {
            if (nums[end] - nums[end - 1] != 1) {
                result.add(getRange(nums, start, end));
                start = end;
            }
        }

        result.add(getRange(nums, start, n));

        return result;
    }

    private String getRange(int[] nums, int start, int end) {
        if (start != end - 1)
            return String.format("%d->%d", nums[start], nums[end - 1]);
        return String.format("%d", nums[start]);
    }
}