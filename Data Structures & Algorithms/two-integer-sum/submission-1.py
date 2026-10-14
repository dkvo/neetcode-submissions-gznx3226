class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        operand_map = {}
        for index, num in enumerate(nums):
            if target - num in operand_map:
                return [operand_map[target -num], index]
            operand_map[num] = operand_map.get(num, 0) + index
        return []