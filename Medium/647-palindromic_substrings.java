class Solution {
    public int countSubstrings(String s) {
        int count = 0;

        for (int i = 0; i < s.length(); i++) {
            count += countSubstrings(s, i, i) +
                     countSubstrings(s, i, i + 1);
        }

        return count;
    }

    public int countSubstrings(String s, int i, int j) {
        if (j >= s.length()) return 0;

        int count = 0;

        while (i >= 0 && j < s.length()) {
            if (s.charAt(i--) != s.charAt(j++)) break;

            count++;
        }
        return count;
    }
}