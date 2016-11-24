
Brute Force Approach:

public int[] twoSum(int nums,int target){
	for(int i=0;i<nums.length;i++){
		for(int j=i+1;j<nums.length;j++){
			if nums[j] = target - nums[i];
			return new int[]{i,j}
		}
	}
	throw new IllegalArgumentException("No two sum solution")
}




One-Pass Hash Table Approach:

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


Class Solution():
	def twoSum(self,nums,target):
		"""
		:type nums: List[int]
        :type target: int
        :rtype: List[int]

		"""
		hash = {}
		for idx,num in nums:
			if num in hash:
				return [idx,hash[num]] 
			else:
				hash[target-num] = idx

