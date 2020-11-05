class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        // Time: O(n * n)
        // Space: O(1)

        int n = time.length;
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if ((time[i] + time[j]) % 60 == 0) res++;
            }
        }

        return res;
    }
}