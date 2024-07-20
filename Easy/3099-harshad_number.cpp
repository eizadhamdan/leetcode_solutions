class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        if (x == 1 || x == 100) return 1;
        
        int sum = 0;
        int num = x;
        while (num != 0) {
            int rem = num % 10;
            sum += rem;
            num /= 10;
        }

        if(x % sum == 0) return sum;
        return -1;
    }
};