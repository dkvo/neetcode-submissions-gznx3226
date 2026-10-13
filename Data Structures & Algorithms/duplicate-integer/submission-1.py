class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}
        for index, val in enumerate(nums):
            if val not in nums_map:
                nums_map[val] = index
            else:
                return True
        return False