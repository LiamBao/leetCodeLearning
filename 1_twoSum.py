from helper import timeit
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.



1：Brute Force Approach:

public int[] twoSum(int nums,int target){
    for(int i=0;i<nums.length;i++){
        for(int j=i+1;j<nums.length;j++){
            if nums[j] = target - nums[i];
            return new int[]{i,j}
        }
    }
    throw new IllegalArgumentException("No two sum solution")
}




2：One-Pass Hash Table Approach:

public int[] twoSum(int nums,int target){
    Map<Integer,Integer> map= new HashMap<>();
    for(int i=0;i<nums.length;i++){
        int complement = target - nums[i];
        if(map.containKey(complement)){
            return new int[]{map.get(complement),i}
        }
        map.put(nums[i],i)
    }
}

3：Python
"""
class Solution():
    @timeit
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        """
        data = {}
        for idx,num in enumerate(nums):
            if num in data:
                return [idx,data[num]] 
            else:
                data[target-num] = idx

s = [1,2,4,23,2,32,23,23,23,23,34,43,42,123,54,4545]
print(str(Solution().twoSum(s, 27)))
