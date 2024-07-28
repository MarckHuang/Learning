class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        j=0          #slow
        for i in range(len(nums)):    #fast
            if nums[i] != val:
                nums[i],nums[j]=nums[j],nums[i]
                j += 1
        return j

nums = [0,1,2,2,3,0,4,2]
val = 2
obj = Solution()
print(obj.removeElement(nums,val))