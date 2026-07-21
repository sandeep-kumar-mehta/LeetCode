class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        w = 0

        for r in range(1, len(nums)):
            if nums[r] != nums[w]:
                w += 1

                nums[w] = nums[r]
        return w + 1