class Solution {
    public int characterReplacement(String s, int k) {
       HashMap<Character, Integer> count = new HashMap<>();
        int res = 0;
        int maxFreq = 0;
        int j = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            count.put(c, count.getOrDefault(c, 0) + 1);

            maxFreq = Math.max(maxFreq, count.get(c));
            int windowSize = i - j + 1;

            if (windowSize - maxFreq > k) {
                char leftChar = s.charAt(j);
                count.put(leftChar, count.get(leftChar) - 1);
                j++;
            }

            res = Math.max(res, i - j + 1);
        }

        return res; 
    }
}