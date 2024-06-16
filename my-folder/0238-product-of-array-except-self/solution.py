class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_length = len(nums)
        result = [1] * array_length

        left_product = 1
        right_product = 1

        for i in range(array_length):
            result[i] = left_product
            left_product *= nums[i]

        for i in range(array_length - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result

