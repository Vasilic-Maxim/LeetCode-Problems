class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        // Time: O(n)
        // Space: O(1)

        int res = 0;
        int n = time.length;
        int[] buckets = new int[60];
        for (int i = 0; i < n; i++) {
            int mod = time[i] % 60;
            int target = (60 - mod) % 60;
            res += buckets[target];
            buckets[mod]++;
        }
        
        return res;
    }
}