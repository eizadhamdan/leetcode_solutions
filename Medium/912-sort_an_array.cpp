class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        mergeSort(nums, 0, nums.size() - 1);
        return nums;
    }
    
    void mergeSort(std::vector<int>& array, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;

            // Sort first and second halves
            mergeSort(array, left, mid);
            mergeSort(array, mid + 1, right);

            // Merge the sorted halves
            merge(array, left, mid, right);
        }
    }

    void merge(std::vector<int>& array, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        // Create temporary arrays
        std::vector<int> leftArray(n1);
        std::vector<int> rightArray(n2);

        // Copy data to temporary arrays leftArray[] and rightArray[]
        for (int i = 0; i < n1; ++i)
            leftArray[i] = array[left + i];
        for (int j = 0; j < n2; ++j)
            rightArray[j] = array[mid + 1 + j];

        // Merge the temporary arrays back into array[left..right]
        int i = 0; // Initial index of first subarray
        int j = 0; // Initial index of second subarray
        int k = left; // Initial index of merged subarray

        while (i < n1 && j < n2) {
            if (leftArray[i] <= rightArray[j]) {
                array[k] = leftArray[i];
                ++i;
            } else {
                array[k] = rightArray[j];
                ++j;
            }
            ++k;
        }

        // Copy the remaining elements of leftArray[], if there are any
        while (i < n1) {
            array[k] = leftArray[i];
            ++i;
            ++k;
        }

        // Copy the remaining elements of rightArray[], if there are any
        while (j < n2) {
            array[k] = rightArray[j];
            ++j;
            ++k;
        }
    }
};
