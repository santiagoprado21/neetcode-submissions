class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            result[i] = product
            product *= nums[i]

        product_rigth = 1

        for i in range(len(nums)-1,-1,-1):
            result[i] *= product_rigth
            product_rigth *= nums[i]
    
        return result