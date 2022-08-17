class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int peak = 0;
        for(int i=1; i<nums.size(); i++) {
            if(nums[i]>nums[i-1])
                peak = i;
        }
        return peak;
    }
};
