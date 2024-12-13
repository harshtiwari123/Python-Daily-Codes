###########################Search location of an element##############################
# 1.Initialize Pointers: Set left = 0 and right = len(nums) - 1.
# 2.Binary Search: While left <= right, calculate mid = (left + right) // 2.
# 3.Compare Target: If nums[mid] == target, return mid. If nums[mid] < target, move left = mid + 1; otherwise, set right = mid - 1.
# 4.Return Position: Return left as the insertion point when the loop ends.
class Solution:
    def searchInsert(self, nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
                
        return left
o1=Solution()
nums = list(map(int, input("Enter integer seprated by spaces ").split()))
target=int(input("Insert the target element"))
print(o1.searchInsert(nums,target))
        

        