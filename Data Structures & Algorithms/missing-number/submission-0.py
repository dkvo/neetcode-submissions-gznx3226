class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

        for i in range(len(nums) + 1):  # ← check 0 to n inclusive
            if i not in hash_map:
                return i

        return 0