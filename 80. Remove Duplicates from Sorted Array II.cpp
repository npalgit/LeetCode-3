// 80. Remove Duplicates from Sorted Array II.cpp
// Time: O(N)
// Space: O(1)

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() <= 2)
            return nums.size();
        int index = 2;
        for (int i = 2; i < nums.size(); ++i) {
            if (nums[i] != nums[index - 2])
                nums[index++] = nums[i];
        }
        return index;
    }
};
