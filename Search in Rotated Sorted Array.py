# # # # # # # # # # # # # # # # #Search in Rotated Sorted Array# # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # Algorithm Steps# # # # # # # # # # # # # # # # # # # 
# 1. Pivot Finding:

# Identify the smallest element (pivot) in the rotated sorted array using binary search.
# If nums[mid] > nums[high], the pivot is in the right part.
# Otherwise, it's in the left part.

# 2. Binary Search:

# Determine in which part of the array (left or right of the pivot) the target lies.
# Perform a standard binary search on that part.

# 3. Integration:

# Combine these two binary searches into a complete solution that works in 𝑂(log𝑛)


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        pivot = low
        low, high = 0, len(nums) - 1
        if nums[pivot] <= target <= nums[high]:
            low = pivot
        else:
            high = pivot - 1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1

nums = list(map(int, input("Enter integer seprated by spaces ").split()))
target=int(input("insert target element"))
o1 = Solution()
print(o1.search(nums,target))
