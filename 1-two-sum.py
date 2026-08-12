def twoSum(self, nums: List[int], target: int) -> List[int]:
        numtrack = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numtrack:
                return [numtrack[complement], i]
            else:
                numtrack[num] = i