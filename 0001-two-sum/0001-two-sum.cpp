#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap; // Stores {value: index}
        
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i]; // What number do we need?
            
            // If the complement is already in the map, return indices
            if (numMap.find(complement) != numMap.end()) {
                return {numMap[complement], i};
            }
            
            // Otherwise, store the current number in the map
            numMap[nums[i]] = i;
        }
        
        return {}; // Should never reach here as per problem constraints
    }
};
